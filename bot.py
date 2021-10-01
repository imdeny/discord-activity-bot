import os

import discord
from discord import activity
from discord.ext import commands
from discord_slash import SlashCommand

import config


def main(): 
    intents = discord.Intents.default()

    activity = discord.Activity(
        type=discord.ActivityType.listening, name="/activity"
    )

    bot = commands.Bot(config.BOT_PREFIX, intents=intents, activity=activity)

    setattr(bot, "slash",
            SlashCommand(bot, override_type=True, sync_commands=True))


    for folder in os.listdir("cogs"):
        if os.path.exists(os.path.join("cogs", folder, "cog.py")):
            bot.load_extension(f"cogs.{folder}.cog")
    

    @bot.event
    async def on_ready():
        """When discord is connected"""
        print(f"{bot.user.name} has connected to Discord!")


    bot.run(config.DISCORD_TOKEN)

if __name__ == "__main__":
    main()