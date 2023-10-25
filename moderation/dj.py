from highrise import *
from highrise.models import *
from config.config import botconfig

async def dj(self: BaseBot, user: User, message: str)-> None:
    if user.username in botconfig.dj:
            pass
    else:
            await self.highrise.chat("vous n'avez pas la permission requise pour cette commande")
            return
    
    #teleports the user to the specified coordinate
    await self.highrise.teleport(user.id, dest = Position(14.5, 16.5 , 10.5))
    print (f"[CMD DJ] teleport (dj) by {user.username} new position = (x = 14.5, y = 16.5, z = 10.5)")