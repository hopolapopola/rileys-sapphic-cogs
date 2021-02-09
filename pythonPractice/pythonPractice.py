import discord
from redbot.core import commands
import random
class pythonPractice(commands.Cog):
    """
    This is Totally Revision :)
    """
    __author__ = ["hopolapopola"]
    __version__ = "yes"

    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def flip(self, ctx: commands.Context, bias):
        """
        Input is an int from 0-100 specifying how biased the flip should be
        """
        try: 
            bias = int(bias)
            result = random.randrange(101)
            if bias < 100:
                if result >= bias: 
                    out_str = "That there is a tails"
                elif result < bias:
                    out_str = "That there is a heads"
        except:
            out_str = "Ah, that wasn't the right input"
        await ctx.send(out_str)        