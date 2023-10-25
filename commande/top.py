from highrise import BaseBot, __main__, CurrencyItem, Item, Position, AnchorPosition, SessionMetadata, User
from highrise.__main__ import BotDefinition
from asyncio import run as arun
from json import load, dump
from highrise.__main__ import *
from highrise.models import *
from config.config import *
from typing import Literal
from highrise import *
import importlib.util
from typing import *
from json import *
from json import *
import asyncio
import os
import asyncio
import os

async def top(self: BaseBot, user: User, message: str,)-> None:
    top_tippers = self.get_top_tippers()
    formatted_tippers = []
    for i, (user_id, user_data) in enumerate(top_tippers):
        username = user_data['username']
        total_tips = user_data['total_tips']
        formatted_tippers.append(f"🏅 {i + 1}  •  {username} [{total_tips}golds]")

        tipper_message = '\n'.join(formatted_tippers)
    await self.highrise.chat(f"\n🏆 Top donnateur SkyClub:\n{tipper_message}")