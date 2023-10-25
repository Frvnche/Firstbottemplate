from highrise import *
from highrise.models import *


async def voicestatus(self, user: User, message: str) -> None:
    voice_status =  await self.highrise.get_voice_status()
    await self.highrise.chat(f"{user.username} le relevée de vocale a etait envoyée dans la console")
    print (voice_status)