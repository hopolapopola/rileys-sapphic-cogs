import discord
from redbot.core import commands
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

class BylethQuotes(commands.Cog):
    """
    Post random Byleth quotes :)
    """
    __author__ = ["hopolapopola"]
    __version__ = "0.0.1"
    
    def __init__(self, bot):
        self.bot = bot
    
    def format_help_for_context(self, ctx: commands.Context) -> str:
        """
            Thanks Sinbad!
        """
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nCog Version: {self.__version__}"
    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    @commands.bot_has_permissions(embed_links=True, add_reactions=True)
    async def crit(self, ctx: commands.Context):
        """Post embed with random Byleth quotes"""
        embed = discord.Embed(colour=discord.Colour.dark_aqua())
        
        message = "\n".join(choice(quotes) for line in range(10))
        if message != "":
            embed.add_field(name=("<:bylethSwag:743093021956112394>"), inline=False)
        embed.set_author(name=("Professor"))
        embed.set_footer(icon_url=("https://cdna.artstation.com/p/assets/images/images/024/428/836/large/kaya-kepa-dancer-byleth-zoom.jpg"))
        # msg = await ctx.send(embed=embed)
        