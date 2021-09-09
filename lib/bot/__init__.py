from lib.cogs.helloworld import helloworld
import discord
from discord import activity
from discord.ext import commands
from discord.ext.commands import Bot as BotBase
from discord.flags import Intents

OWNER_IDS = [477949541337792524]
MODULES = ["helloworld"]

class Bot(BotBase):
    def __init__(self):
        super().__init__(command_prefix="-", intents=discord.Intents.all(), owner_ids=OWNER_IDS, activity=discord.Game(name="-help"))
    
    def setup(self):
        for cog in MODULES:
            self.load_extension(f"lib.cogs.{cog}")
        
    def run(self, token):
        self.setup()
        self.TOKEN = token
        super().run(self.TOKEN, reconnect=True)
    
    async def on_ready(self):
        print("conectado")

bot = Bot()