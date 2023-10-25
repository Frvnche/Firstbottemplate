from highrise import *
from highrise.models import *
from config.config import botconfig

async def vip(self: BaseBot, user: User, message: str)-> None:
    if user.username in botconfig.ownername:
            pass
    elif user.username in botconfig.moderateur:
            pass
    elif user.username in botconfig.contributeur:
            pass
    else:
            await self.highrise.chat("vous n'avez pas la permission requise pour cette commande")
            return
    
    #teleports the user to the specified coordinate
    await self.highrise.teleport(user.id, dest = Position(12.5, 14.0 , 22.5))
    print (f"[CMD VIP] teleport (vip) by {user.username} new position = (x = 15.5, y = 14.0, z = 22.5)")