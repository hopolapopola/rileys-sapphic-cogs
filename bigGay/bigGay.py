import discord
import asyncio
import string
from typing import Any, List, Tuple
from redbot.core import commands
from redbot.core.utils import common_filters
from redbot.core.utils.chat_formatting import box

async def type_message(
        destination: discord.abc.Messageable, content: str, **kwargs
    ) -> discord.Message:
        """Simulate typing and sending a message to a destination.
        Will send a typing indicator, wait a variable amount of time based on the length
        of the text (to simulate typing speed), then send the message.
        """
        content = common_filters.filter_urls(content)
        try:
            async with destination.typing():
                await asyncio.sleep(max(0.25, min(2.5, len(content) * 0.01)))
                return await destination.send(content=content, **kwargs)
        except discord.HTTPException:
            pass

async def reply(ctx: commands.Context, content: Any = None, **kwargs: Any):
    """Safely reply to a command message.
    If the command is in a guild, will reply, otherwise will send a message like normal.
    Pre discord.py 1.6, replies are just messages sent with the users mention prepended.
    """
    if ctx.guild:
        if (
            hasattr(ctx, "reply")
            and ctx.channel.permissions_for(ctx.guild.me).read_message_history
        ):
            mention_author = kwargs.pop("mention_author", False)
            kwargs.update(mention_author=mention_author)
            await ctx.reply(content=content, **kwargs)
        else:
            allowed_mentions = kwargs.pop(
                "allowed_mentions",
                discord.AllowedMentions(users=False),
            )
            kwargs.update(allowed_mentions=allowed_mentions)
            await ctx.send(content=f"{ctx.message.author.mention} {content}", **kwargs)
    else:
        await ctx.send(content=content, **kwargs)   

class bigGay(commands.Cog):
    """
    The Big Gay is me :)
    """
    __author__ = ["hopolapopola"]
    __version__ = "1.1"
    
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
    
    @commands.command()
    async def unoreverse(self, ctx: commands.Context, *, text: str = None):
        """Uno reverse card, but for text in messages"""
        if not text:
            if hasattr(ctx.message, "reference") and ctx.message.reference:
                try:
                    text = (
                        await ctx.fetch_message(ctx.message.reference.message_id)
                    ).content
                except (discord.Forbidden, discord.NotFound, discord.HTTPException):
                    pass
            if not text:
                text = (await ctx.channel.history(limit=2).flatten())[
                    1
                ].content or "I can't reverse that!\n https://thumbs.gfycat.com/WellwornYearlyGossamerwingedbutterfly-max-1mb.gif"
        await type_message(
            ctx.channel,
            self.reverse(text),
            allowed_mentions=discord.AllowedMentions(
                everyone=False, users=False, roles=False
            ),
        )

    @commands.command()
    async def boringreverse(self, ctx: commands.Context, input):
        i = input.length
        output = ""
        if output.length > 0:
            while (i > -1):
                output += input[i]
                i-=1
        else:
            output="piss"
        await ctx.send(output)
        
