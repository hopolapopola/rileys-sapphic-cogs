import discord
from redbot.core import commands
import random

class transBot(commands.Cog):
    """
    mfw i literally recreate TransBot in like, an hour idk how long this will take but we shall see :))

    also i'm not reusing code so don't @ me 
    """
    __author__ = ["hopolapopola"]
    __version__ = "1.1"

    def __init__(self,bot):
        self.bot = bot

    
    def createWallOfText(pronouns):
        paragraphs = [
        	(pronouns[0]+" is super cool and "+pronouns[3]+" style is very unique."),
            ("I want to be "+pronouns[0]+"'s friend, "+pronouns[1]+" seem like a lovely person :)"),
            ("I want to be "+pronouns[0]+"'s friend, "+pronouns[1]+" seems like a lovely person :)"),
            (pronouns[0]+" has a cool haircut and "+pronouns[3]+" shoes are lit!"),
            (pronouns[0]+" is such a great name!"+pronouns[0]+" chose "+pronouns[3]+" name "+pronouns[5]+" just makes "+pronouns[1]+" even cooler :3"),
        ]
        choice = random.randrange(1, 4)   
        if choice == 1:
            text = paragraphs[0]
        elif choice == 2:
            if pronouns[6] == 0:
                text = paragraphs[1]
            else:
                text = paragraphs[2]
        elif choice == 3:
            text = paragraphs[3]
        elif choice == 4:
            text = paragraphs[4]
        else:
            text = "something happened"
        return text

    @commands.command()    
    async def pronouns(self, ctx: commands.Context, name, p1, p2, p3, p4):
        if (p1 == "he") or (p1 == "she") or (p1 == "it"):
            type = 1
        else: 
            type = 0
        pronouns = [name, p1, p2, p3, p4, p2+"self", type]
        message = transBot.createWallOfText(pronouns)
        await ctx.send(message)
