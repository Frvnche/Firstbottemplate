from highrise import *
from highrise.webapi import *
from highrise.models_webapi import *
from highrise.models import *


async def getpos(self, user: User, message: str) -> None:
    room_users = (await self.highrise.get_room_users()).content
    for room_user, position in room_users:
            if room_user.username.lower() == user.username.lower():
                user_position = position
                break
    await self.highrise.chat(f"Position imprimée dans la console")
    print(f"voici la position de {user.username} : {user_position}")