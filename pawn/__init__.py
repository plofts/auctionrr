import discord
from .pawn import PawnStoreCore

async def setup(bot):
    cog = PawnStoreCore(bot)
    if discord.__version__ == "1.7.3":
        bot.add_cog(cog)
    else:
        await bot.add_cog(cog)