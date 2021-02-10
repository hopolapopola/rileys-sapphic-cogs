import discord
from redbot.core import commands
import random
from datetime import date
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
                    outStr = "That there is a tails"
                elif result < bias:
                    outStr = "That there is a heads"
            else:
                outStr = "cheeky. but nope, not gonna work"
        except:
            outStr = "Ah, that wasn't the right input"
        await ctx.send(outStr)
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
                    outStr = str(x + y)
                elif operator == '-':
                    outStr = str(x - y)
                elif operator == '/':
                    outStr = str(x / y)
                elif operator == 'x':
                    outStr = str(x * y)
                else:
                    outStr = "oops, operator machine :b:roke"
            elif type == "str":
                if operator == "+":
                    outStr = str(x + y)
                else:
                    outStr = "Big chungus is disappointed in you"
            else:
                outStr = type
        except:
            outStr = "http://www.lovemysurface.net/wp-content/uploads/2015/07/Windows-10-Upgrade-Error-Something-Happened.jpg"
        await ctx.send(outStr)
    @commands.command()
    async def isleap(self, ctx: commands.Context, year):
        """
        Determines whether a year after 0CE is a leap year or not :)
        """
        curYear = date.today()
        leapYear = False
        try:
            year = int(year)
            if year % 4 == 0:
                if year % 100:
                    if year % 400 == 0:
                        leapYear = True
                    else:
                        leapYear = False
                else: 
                    leapYear = True
            else:
                leapYear = False
        except:
            outStr = "Need to input a year as an integer :)"
        if leapYear:
            if year > curYear.year:
                outStr = str(year) + " will be a leap year <:KannaRise:706697896292253728>"
            elif year == curYear.year:
                outStr = str(year) + " is a leap year <:KannaRise:706697896292253728>"
            else:
                outStr = str(year) + " was a leap year <:KannaRise:706697896292253728>"
        else: 
            if year > curYear.year:
                outStr = str(year) + " will not be a leap year <:BigYui3:784248022174793728>"
            elif year == curYear.year:
                outStr = str(year) + " isn't a leap year <:BigYui3:784248022174793728>"
            else:
                outStr = str(year) + " was not a leap year <:BigYui3:784248022174793728>"
        await ctx.send(outStr)
    @commands.command()
    async def triangle(self, ctx: commands.Context, num):
        """
        triangular numbers for some reason?
        """
        try:
            i = 1
            total = 0    
            while total < int(num):
                total += i
                i += 1
        except:
            outStr = "pp"    
        outStr = str(total)
        await ctx.send(outStr)
