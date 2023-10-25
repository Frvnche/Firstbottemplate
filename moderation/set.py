from highrise import *
from highrise.models import *


async def set(self, user: User, message: str) -> None:
    set_position = await self.set_bot_position(user.id)
    await self.highrise.chat(f"Updated bot position to {user.username}.")
    return set_position