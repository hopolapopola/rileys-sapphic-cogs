from .bigGay import bigGay

def setup(bot):
    cog = bigGay(bot)
    bot.add_cog(cog)