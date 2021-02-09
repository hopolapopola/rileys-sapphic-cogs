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
            if (bias <= 100) and (bias >= 0):
                if result >= bias: 
                    out_str = "That there is a tails"
                elif result < bias:
                    out_str = "That there is a heads"
            else:
                out_str = "cheeky. but nope, not gonna work"
        except:
            out_str = "Ah, that wasn't the right input"
        await ctx.send(out_str)
    @commands.command()
    async def calc(self, ctx: commands.Context, x, operator, y, type="int"):
        """
        Input is a string (with spaces) containing +, -, /, or x for the 4 basic operators, with optional arg for int or str operation
        """
        try:
            if type == "int":
                x = int(x)
                y = int(y)
            if operator == '+':
                out_str = str(x + y)
            elif operator == '-':
                out_str = str(x - y)
            elif operator == '/':
                out_str = str(x / y)
            elif operator == 'x':
                out_str = str(x * y)
            else:
                out_str = "oops, operator machine :b:roke"
        except:
            out_str = "http://www.lovemysurface.net/wp-content/uploads/2015/07/Windows-10-Upgrade-Error-Something-Happened.jpg"
        await ctx.send(out_str)