import discord, logging, tokens

class DanDroid(discord.Client):
    async def on_ready(self):
        logger.info("Logged on as " + str(self.user))

logger = logging.getLogger()
handler = logging.FileHandler("dandroid.log", mode="a")
formatter = logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

client = DanDroid()
client.run(tokens.discord)