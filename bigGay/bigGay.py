import discord
from redbot.core import commands

class bigGay(commands.Cog):
    """
    The Big Gay is me :)
    """
    __author__ = ["hopolapopola"]
    __version__ = "1.0g"
    
    def __init__(self, bot):
        self.bot = bot
    
    async def gay(self, ctx: commands.Context, the_gay):
        """
        Be gay, do gay
        """
        out_num = 0
        out_str = ""
        try: 
            for letter in the_gay:
                out_num += string.ascii_letters.index(letter)
                if string.ascii_letters.index(letter) != 0: 
                    out_num /= string.ascii_letters.index(letter)
            if (out_num % 2) == 0:
                out_str.append("you have the Big Gay")
            elif (out_num / 100) > 1:
                out_str.append("pingu")
            elif (out_num ** 2) < 100: 
                out_str.append("https://ebay.com")
            elif out_num == 1:
                out_str.append("<:redditmoment:686443293873012776><:redditmoment:686443293873012776><:redditmoment:686443293873012776>\n<:redditmoment:686443293873012776> <:redditmoment:686443293873012776>\n<:redditmoment:686443293873012776><:redditmoment:686443293873012776><:redditmoment:686443293873012776>")
            else:
                out_str.append("try again.")
        except: 
            out_str.append("use latin alphabet only!")
        await ctx.send(out_str)
        