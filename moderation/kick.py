from highrise import *
from highrise.webapi import *
from highrise.models_webapi import *
from highrise.models import *
from config.config import botconfig

async def kick(self, user: User, message: str) -> None:
    if user.username in botconfig.moderateur:
        pass
    else:
        await self.highrise.chat("vous n'avez pas la permission requise pour cette commande")
        return
    #separete message into parts
    parts = message.split()
    if len(parts) != 2:
        await self.highrise.chat("vous avez mal formuler la commande Kick.")
        return
    #checks if there's a @ in the message
    if "@" not in parts[1]:
        username = parts[1]
    else:
        username = parts[1][1:]
    #check if user is in room
    room_users = (await self.highrise.get_room_users()).content
    for room_user, pos in room_users:
        if room_user.username.lower() == username.lower():
            user_id = room_user.id
            break
    if "user_id" not in locals():
        await self.highrise.chat("Utilisateur introuvable, s'il vous plait mentionner un utilisateur.")
        return
    try:
        await self.highrise.moderate_room(user_id, "kick")
    except Exception as e:
        await self.highrise.chat(f"{e}")
        return
    #send message to chat
    await self.highrise.chat(f"{username} a etait expulser de la room par {user.username}.")
    print (f"[CMD MOD] Kick by {user.username} for kick {room_user.username}")