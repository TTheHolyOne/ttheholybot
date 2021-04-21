import os, sys, discord, platform, random, aiohttp, json
from discord.ext import commands

if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class general(commands.Cog, name="important"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="program", aliases=["programs"])
    async def info(self, context):
        """
       Programs ttheholyone has made
        """
        embed = discord.Embed(
            description="TTheHolyBot",
            color=config.success
        )
        embed.set_author(
            name="Programs"
        )
        embed.add_field(
            name="Owner:",
            value="TTheHolyOne#1642\n",
            inline=True
        )
        embed.add_field(
            name="Programs:",
            value="A list of my programs are:\n• Python - Calculator\n• Python - Temperature Converter\n• Python - Mad Libs Generator\n• Python - Story Game\n• Python - Number Guessing Game\n• Python - Wifi Password Grabber\n• Python - Password Generator\n• Python - Sorter\n• Javascript - Discord Bot\n\nAnd many more.."
        )
        embed.add_field(
            name="Socials:",
            value="https://www.ttheholyone.com\nhttps://www.github.com/ttheholyone",
            inline=True
        
        )
        embed.add_field(
            name="Python Version I use:",
            value=f"{platform.python_version()}",
            inline=True
        )
        embed.add_field(
            name="Prefix:",
            value=f"{config.BOT_PREFIX}",
            inline=False
        )
        embed.set_footer(
            text=f"Requested by {context.message.author}"
        )
        await context.send(embed=embed)
def setup(bot):
    bot.add_cog(general(bot))