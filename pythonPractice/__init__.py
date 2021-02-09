from .pythonPractice import pythonPractice

def setup(bot):
    cog = pythonPractice(bot)
    bot.add_cog(cog)
