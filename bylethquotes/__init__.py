from .bylethquotes import BylethQuotes

def setup(bot):
    cog = BylethQuotes(bot)
    bot.add_cog(cog)
