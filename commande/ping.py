from highrise import *
from highrise.models import *
from config.config import botconfig
import time


async def ping(self, user: User, message : str):
    # Send a message to simulate bot activity
    start_time = time.time()
    end_time = time.time()

    # Calculate and print the bot's ping
    # Convert to milliseconds
    ping = round((end_time - start_time) * 1000)
    await self.highrise.chat(f'Bot ping: {ping}ms')
    print (f"[CMD] ping by {user.username} (bot ping:{ping}ms)")