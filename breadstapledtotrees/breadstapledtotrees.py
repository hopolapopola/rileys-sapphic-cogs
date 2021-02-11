import discord
from redbot.core import commands
from random import choice
from typing import List

images: List[str] = [
    ("https://i.redd.it/4ww01w9het941.jpg"),
    ("https://i.redd.it/pdk9qn23pso11.jpg"),
    ("https://i.redd.it/nczlcfbujcm31.jpg"),
    ("https://i.redd.it/tvkcucayqw931.jpg"),
    ("https://i.redd.it/kh3vywyii5l51.jpg"),
    ("https://i.redd.it/faljvxa4nhq51.jpg"),
    ("https://i.redd.it/swqjs89frss31.jpg"),
    ("https://i.redd.it/nw76w395csf41.jpg"),
    ("https://i.redd.it/rk0nek836bs01.png"),
    ("https://i.redd.it/3cezccnrjd041.jpg"),
    ("https://i.redd.it/6yxaqpesect01.jpg"),
    ("https://i.redd.it/5jc0atew72441.png"),
    ("https://i.redd.it/7bi9m3das0811.png"),
    ("https://i.redd.it/0kcg81aadev21.jpg")
]

class BreadStapledToTrees(commands.Cog):
    __author__ = ["MayaValentia"]
    __version__ = "1"
    
    def __init__(self, bot):
        self.bot = bot
    
    def format_help_for_context(self, ctx: commands.Context) -> str:
        """
            Thanks Sinbad!
        """
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nCog Version: {self.__version__}"

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def bread(self, ctx: commands.Context):
        await ctx.send(choice(images))