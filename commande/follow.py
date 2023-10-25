from highrise import *
from highrise.models import *
from config.config import botconfig
import asyncio

async def follow(self: BaseBot, user: User, message: str) -> None:
    if user.username in botconfig.moderateur:
        pass
    elif user.username in botconfig.contributeur:
        pass
    elif user.username in botconfig.ownername:
        pass
    else:
        await self.highrise.chat("vous n'avez pas la permission requise pour cette commande")
        return
    taskgroup = self.highrise.tg
    task_list = list(taskgroup._tasks)
    for task in task_list:
        if task.get_name() == "following_loop":
            await self.highrise.chat("je suis déjà quelqu'un")
            return
    #checks if this function is already in the Highrise class tg (task group).
    taskgroup.create_task(coro=following_loop(self, user, message), name = "following_loop")
    await self.highrise.chat(f"je suis! {user.username}")
    print (f"[CMD] follow by {user.username}")
    
async def stop(self: BaseBot, user: User, message: str) -> None:
    taskgroup = self.highrise.tg
    task_list = list(taskgroup._tasks)
    for task in task_list:
        if task.get_name() == "following_loop":
            task.cancel()
            await self.highrise.chat(f"j'arrête de suivre {user.username}")
            print (f"[CMD] stop by {user.username}")
            return
    await self.highrise.chat("je ne suis personne")
    return

async def following_loop(self: BaseBot, user: User, message: str) -> None:
    if message.startswith(f"{botconfig.prefix}following_loop"):
        await self.highrise.chat(f"commande invalide, s'il te plait utilise {botconfig.prefix}follow")
        return
    while True:
        #gets the user position
        room_users = (await self.highrise.get_room_users()).content
        for room_user, position in room_users:
            if room_user.id == user.id:
                user_position = position
                break
        if type(user_position) != AnchorPosition:
            await self.highrise.walk_to(Position(user_position.x + 1, user_position.y, user_position.z))
        await asyncio.sleep(0.5)