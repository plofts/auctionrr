import discord
import aiohttp
from redbot.core import commands, app_commands, Config


class PawnStoreCore(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=83153214)
        default_global = {
            "pawn_db_url": "localhost",
            "pawn_db_user": "root",
            "pawn_db_password": "",
            "pawn_db_name": "",
        }
        self.config.register_global(**default_global)

    setup = app_commands.Group(name="setup", description="Setup the database for PawnStore")
    
    def owner_only(interaction:discord.Interaction) -> bool:
        return interaction.user.id == discord.AppInfo.owner
    
    @setup.command(name="uri")
    @app_commands.check(owner_only)
    async def _uri(self, interaction: discord.Interaction, uri: str):
        """Set the database URI"""
        await interaction.response.send_message(uri)
