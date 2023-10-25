from highrise import *
from highrise.models import *
from config.config import botconfig

async def tpto(self: BaseBot, user: User, message: str,)-> None:
    #permission moderateur obligatoire
    if user.username in botconfig.moderateur:
        pass
    elif user.username in botconfig.contributeur:
        pass
    elif user.username in botconfig.ownername:
        pass
    else:
        await self.highrise.chat("vous n'avez pas la permission requise pour cette commande")
        return
    
    parts = message.split()
    if len(parts) != 2:
        await self.highrise.chat(f"vous avez mal formuler la commande. \nEsseaye {botconfig.prefix}tpto [@username]")
        return
    #checks if there's a @ in the message
    if "@" not in parts[1]:
        username = parts[1]
    else:
        username = parts[1][1:]
    #check if user is in room
    room_users = (await self.highrise.get_room_users()).content
    for room_user, position in room_users:
            if room_user.username.lower() == username.lower():
                user_position = position
                break
    if "room_user" not in locals():
        await self.highrise.chat("Utilisateur introuvable, s'il vous plait mentionner un utilisateur.")
        return
    try:
        if type(user_position) != AnchorPosition:
            await self.highrise.teleport(user.id, Position(user_position.x, user_position.y, user_position.z))
    except Exception as e:
        await self.highrise.chat(f"{e}")
        return
    #send message to chat
    print (f"[CMD] teleport (tpto) by {user.username} to {room_user.username}")
    
    
