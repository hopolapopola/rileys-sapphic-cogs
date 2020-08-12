import discord
from redbot.core import commands
#from redbot.core.il8n import Translator, cog_il8n
from random import choice
from typing import List


quotes: List[str] = [
    ("Each battle is a chance to grow"),
    ("Stay focused."),
    ("I'm not setting a very good example."),
    ("We must all do our part."),
    ("I'm stronger than before."),
    ("I've finally realized my potential."),
    ("Not my best."),
    ("I'll use this power for the greater good."),
    ("There is still room for improvement."),
    ("Another step forward."),
    ("It seems I've reached my full potential."),
    ("The glory of progress."),
    ("Practice yields results."),
    ("I still have much to learn."),
    ("Such power dwells within?"),
    ("There is still more to learn."),
    ("This experience is critical."),
    ("I'm getting the hang of this."),
    ("I'll use this power for the greater good."),
    ("It seems I've exhausted this topic."),
    ("I've fully grasped this topic."),
    ("Practice yields results."),
    ("A new path to tread."),
    ("I'm not setting a very good example."),
    ("I've set my sights higher."),
    ("Not my best."),
    ("It seems I've exhausted this topic."),
    ("I've fully grasped this topic."),
    ("What a strange feeling."),
    ("It's time to start anew."),
    ("I've set my sights higher."),
    ("I must keep learning."),
    ("I've set my sights higher."),
    ("I hope to master this quickly."),
    ("Stay focused."),
    ("Be mindful."),
    ("Careful now."),
    ("What's my strategy?"),
    ("I must pull through."),
    ("I may not survive."),
    ("Predictable."),
    ("Watch and learn!" ),
    ("Let the lesson begin!"),
    ("Allow me to demonstrate!"),
    ("No hesitation!"),
    ("It's over!"),
    ("Here is something to believe in!"),
    ("Here is your answer!"),
    ("Prepare yourself!"),
    ("Let this be a lesson!"),
    ("Now's our chance."),
    ("It's time."),
    ("We've got to try."),
    ("I'm here to help."),
    ("You're covered."),
    ("We'll cover you."),
    ("Our power is yours."),
    ("I won't fail you."),
    ("We'll protect you." ),
    ("Everyone! It's time"),
    ("Together!"),
    ("We fight as one."),
    ("Should I have held back?"),
    ("You fought well."),
    ("That is that."),
    ("Each battle is a chance to grow."),
    ("As expected."),
    ("You didn't give it your all." ),
    ("This could turn the tides."),
    ("It won't be in vain."),
    ("Another victory."),
    ("All is going to plan."),
    ("I must lead them well."),
    ("There's no turning back now."),
    ("Just like that."),
    ("Keep it up."),
    ("I'm impressed."),
    ("Truly impressive."),
    ("I knew you can do it."),
    ("We won't back down."),

]
images: List[str] = [
    ("https://i.redd.it/r18lmn76jaj41.jpg"),
    ("https://i.imgur.com/kMMe4x4.jpg"),
    ("https://i.imgur.com/NY9rgTj.jpg"),
    ("https://i.imgur.com/9airR1C.jpg"),
    ("https://i.redd.it/f5r6zj29k4551.jpg"),
]
images_all: List[str] = [
    ("https://i.redd.it/r18lmn76jaj41.jpg"),
    ("https://i.imgur.com/kMMe4x4.jpg"),
    ("https://i.imgur.com/NY9rgTj.jpg"),
    ("https://i.imgur.com/9airR1C.jpg"),
    ("https://i.redd.it/f5r6zj29k4551.jpg"),
    ("https://i.redd.it/0q9uplumf8s41.jpg"),
    ("https://i.imgur.com/DX5K3p1.jpg"),
    ("https://i.redd.it/eojhr24bb8z41.jpg"),
]
images_edeleth: List[str] = [
    ("https://cdn.discordapp.com/attachments/743117606919340124/743118342608519168/image0.jpg"),
    ("https://cdn.discordapp.com/attachments/743117606919340124/743118342818103346/image1.jpg"),
    ("https://cdn.discordapp.com/attachments/743117606919340124/743118343011172443/image2.jpg"),
    ("https://cdn.discordapp.com/attachments/743117606919340124/743118343271350302/image3.jpg"),
    ("https://cdn.discordapp.com/attachments/743117606919340124/743118414918189096/image0.jpg"),
    ("https://cdn.discordapp.com/attachments/743117606919340124/743118567897039020/IMG_0967.JPG"),
    ("https://cdn.discordapp.com/attachments/743117606919340124/743118723841523822/IMG_0931.JPG"),
    ("https://cdn.discordapp.com/attachments/743117606919340124/743118835187449986/IMG_0881.JPG"),
]
#@cog_il8n
class BylethQuotes(commands.Cog):
    """
        Post random Byleth quotes :)
    """
    __author__ = ["hopolapopola"]
    __version__ = "0.1"
    
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
    @commands.bot_has_permissions(embed_links=True)
    async def quote(self, ctx: commands.Context):
        """Post embed with random Byleth quotes"""
        embed = discord.Embed(colour=discord.Colour.green())
        message = "\n".join(choice(quotes) for line in range(1))
        image = "\n".join(choice(images) for line in range (1))
        if message != "":
            embed.add_field(name=("<:bylethSwag:743093021956112394>"), value=message, inline=True)
        embed.set_author(name=("Professor"))
        embed.set_image(url=image)
        await ctx.send(embed=embed)
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def byleth(self, ctx: commands.Context):
        image = "\n".join(choice(images_all) for line in range (1))
        embed = discord.Embed(colour=discord.Colour.green())
        embed.set_image(url=image)
        await ctx.send(embed=embed)
    @commands.command(aliases=["maya", "riley"])
    @commands.bot_has_permissions(embed_links=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def edeleth(self, ctx: commands.Context):
        image = "\n".join(choice(images_edeleth) for line in range (1))
        embed = discord.Embed(colour=discord.Colour.green())
        embed.set_image(url=image)
        await ctx.send(embed=embed)
    @commands.command()
    async def edelgard(self, ctx: commands.Context):
        message = "I love my wife <:bylethPillow:743120663715250227> <:bylethHeart:743120792346296400>"
        await ctx.send(message)
    @commands.command(aliases=["michelle"])
    async def ssb(self, ctx: commands.Context):
        message = "I would beat <@!277183660636110859> in a 1v1 BF no items 3 stock 8 minutes."
        await ctx.send(message)