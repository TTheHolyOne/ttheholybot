import os, sys, discord, platform, random, aiohttp, json
from discord.ext import commands

# Only if you want to use variables that are in the config.py file.
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

# Here we name the cog and create a new class for the cog.
class Template(commands.Cog, name="holyornot"):
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.
   
    @commands.command(name="holy")
    async def eight_ball(self, context, *args):
        """
        Sees if you are holy.
        """
        answers = ['Very!', 'No... get out of here you demon', 'Yes!', 'I guess so...', 'OH MY GOD YOU ARE THE HOLY ONE']
        embed = discord.Embed(
            title="**Holy or Not: ",
            description=f"{answers[random.randint(0, len(answers))]}",
            color=config.success
        )
        embed.set_footer(
            text=f"Question asked by: {context.message.author}"
        )
        await context.send(embed=embed)

# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
def setup(bot):
    bot.add_cog(Template(bot))