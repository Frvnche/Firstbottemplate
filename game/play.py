from highrise import *
from highrise.models import *
from config.config import botconfig

async def play(self, user: User,  message: str):
    await self.highrise.chat(f"@{user.username} les commande de jeux ne sont pas encore accesible")