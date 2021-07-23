from discord import Intents
from discord.ext.commands import Bot
import discord
from Cogs import Check

import os

from dotenv import load_dotenv
load_dotenv()

bot = Bot(command_prefix='$')

bot.add_cog(Check.Cog(bot, int(os.environ['CHANNEL'])))
bot.run(os.environ['TOKEN'])
