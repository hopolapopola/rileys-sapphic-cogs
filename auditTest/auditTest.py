import discord
from redbot.core import commands

class AuditTest(commands.Cog):
    """
        Test out how the audit log actions are returned
        THE HELP COMMAND DOES NOTHING
    """
    __author__ = ["hopolapopola"]
    __version__ = "0.1b"

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.guild)
    @commands.bot_has_permissions(embed_links=True)
    async def listActions(ctx: commands.Context):
        embed = discord.Embed(colour=discord.Colour.green())
        action = discord.AuditLogAction
        i = 1
        async for entry in discord.Guild.audit_logs(user=None, limit=5):
            formatted_entry = '{0.user} did {0.action} to {0.target}'.format(entry)
            embed.add_field(name=str(i), value=formatted_entry)
        await ctx.send(embed=embed)