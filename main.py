import discord, logging, tokens, phrases, random, asyncio
from datetime import datetime

class DanDroid(discord.Client):
    # config
    prefix = "dandy " # nb: prefix includes space
    awake = True
    counter = 1

    async def send_message(self, message, response):
        await asyncio.sleep(random.randint(1,3))
        await message.channel.trigger_typing()
        await asyncio.sleep(random.randint(3,6))
        await message.channel.send(response)

    async def on_ready(self):
        logger.info("Logged on as " + str(self.user))
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        
        elif message.content.startswith(self.prefix):
            if "sleep" in message.content[len(self.prefix):]:
                if self.awake == True:
                    self.awake = False
                    logger.info("Bot was awake, now asleep")
                    
                    if datetime.now().hour < 7:
                        time_of_day = "night"
                    elif datetime.now().hour < 12:
                        time_of_day = "morning"
                    elif datetime.now().hour < 18:
                        time_of_day = "afternoon"
                    else:
                        time_of_day = "night"
                    
                    response = random.choice(phrases.sleeping)

                    if "[x]" in response:
                        response = response.replace("[x]", time_of_day)

                    await message.channel.send(response)
                    return
                else:
                    await self.send_message(message, "I'm already asleep haha")
                    return
                    

            if "wake" in message.content[len(self.prefix):]:
                if self.awake == False:
                    self.awake = True
                    logger.info("Bot was asleep, now awake")

                    if datetime.now().hour < 7:
                        time_of_day = "night"
                    elif datetime.now().hour < 12:
                        time_of_day = "morning"
                    elif datetime.now().hour < 18:
                        time_of_day = "afternoon"
                    else:
                        time_of_day = "night"
                    
                    response = random.choice(phrases.waking)

                    if "[x]" in response:
                        response = response.replace("[x]", time_of_day)

                    await self.send_message(message, response)
                    return
                else:
                    await self.send_message(message, "I'm already awake duhhh")
                    return
            
            if self.awake == False:
                await self.send_message(message, "shhh I'm trying to sleep!")
            else:
                if "hello" in message.content[len(self.prefix):]:
                    await self.send_message(message, "hello, {0}! nice to meet you!".format(str(message.author)[:-5]))

        else:
            if self.awake == False:
                return
            else:
                if self.counter < 20:
                    self.counter = self.counter + 1
                    return
                else:
                    self.counter = 1
                    if random.randint(0, 100) < 10:
                        response = random.choice(phrases.generic)
                        await self.send_message(message, response)
                
                
        
        

logger = logging.getLogger()
handler = logging.FileHandler("dandroid.log", mode="a")
formatter = logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

client = DanDroid()
client.run(tokens.discord)