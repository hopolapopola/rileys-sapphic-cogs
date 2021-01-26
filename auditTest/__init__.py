from .auditTest import AuditTest

def setup(bot):
    cog = AuditTest(bot)
    bot.add_cog(cog)