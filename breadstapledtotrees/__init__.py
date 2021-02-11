from .breadstapledtotrees import BreadStapledToTrees

def setup(bot):
    cog = BreadStapledToTrees(bot)
    bot.add_cog(cog)
