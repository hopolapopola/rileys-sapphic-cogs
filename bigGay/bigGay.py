import discord
import string
from redbot.core import commands

class bigGay(commands.Cog):
    """
    The Big Gay is me :)
    """
    __author__ = ["hopolapopola"]
    __version__ = "1.0g"
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def gay(self, ctx: commands.Context, the_gay):
        """
        Be gay, do gay
        """
        out_num = 0
        out_str = " "
        try: 
            for letter in the_gay:
                out_num += string.ascii_letters.index(letter)
                # if string.ascii_letters.index(letter) != 0: 
                #     out_num /= string.ascii_letters.index(letter)
            if (out_num % 2) == 0:
                out_str = "you have the Big Gay"
            elif (out_num / 100) > 1:
                out_str = "pingu"
            elif (out_num ** 2) > 100: 
                out_str = "https://ebay.com"
            elif out_num == 1:
                out_str = "<:redditmoment:805272210704826379><:redditmoment:805272210704826379><:redditmoment:805272210704826379>\n<:redditmoment:805272210704826379> <:redditmoment:805272210704826379>\n<:redditmoment:805272210704826379><:redditmoment:805272210704826379><:redditmoment:805272210704826379>"
            else:
                out_str = "try again."
        except: 
            out_str = "use latin alphabet only!"
        message = out_str
        await ctx.send(message)
    @commands.command()
    async def intest(self, ctx: commands.Context, input, in2, in3):
        message = input + " " + in2 + " " + in3
        await ctx.send(message)  