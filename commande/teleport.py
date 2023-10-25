from highrise import *
from highrise.models import *
from config.config import botconfig

async def teleport(self: BaseBot, user: User, message: str)-> None:
    if user.username in botconfig.moderateur:
            pass
    elif user.username in botconfig.contributeur:
            pass
    elif user.username in botconfig.ownername:
            pass
    else:
            await self.highrise.chat("vous n'avez pas la permission requise pour cette commande")
            return
    try:
        command, username, coordinate = message.split(" ")
    except:
        await self.highrise.chat("Incorrect format, please use /teleport <username> <x,y,z>")
        return
    
    #checks if the user is in the room
    room_users = (await self.highrise.get_room_users()).content
    for user, _ in room_users:
        if user.username.lower() == username.lower():
            user_id = user.id
            break
    #if the user_id isn't defined, the user isn't in the room
    if "user_id" not in locals():
        await self.highrise.chat("User not found, please specify a valid user and coordinate")
        return
        
    #checks if the coordinate is in the correct format (x,y,z)
    try:
        x, y, z = coordinate.split(",")
    except:
        await self.highrise.chat("Coordinate not found or incorrect format, please use x,y,z")
        return
    
    #teleports the user to the specified coordinate
    await self.highrise.teleport(user_id = user_id, dest = Position(float(x), float(y), float(z)))
    print (f"[CMD] teleport (manuelle) by {user.username}")