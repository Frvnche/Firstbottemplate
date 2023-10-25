### FILL IN YOUR ROOM ID & API KEY HERE
room_id = "65241d2ef9e03318489ea787"
api_key  = "9188ddb039510ca304bdb89eba4c975a87e27e4fee261ce3b26b56b65b17f2e9"

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

class Bot(BaseBot):
    def __init__(self):
        super().__init__()
        self.bot_id = None
        self.owner_id = None
        self.bot_status = False
        self.tip_data = None
        self.load_tip_data()
        self.bot_position = None

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username} said: {message}")
        if message.startswith(f"{botconfig.prefix}"):
            await self.command_command(user, message)
            await self.command_outfit(user, message)
            await self.command_moderation(user, message)
        response = await self.command_handler(user.id, message)
        if response:
            try:
                await self.highrise.chat(response)
            except Exception as e:
                print(f"Chat Error: {e}")

    async def on_whisper(self, user: User, message: str) -> None:
        print(f"{user.username} whispered: {message}")
        response = await self.command_handler(user.id, message)
        if response:
            try:
                await self.highrise.send_whisper(user.id, response)
            except Exception as e:
                print(f"Whisper Error: {e}")

    async def on_message(self, user_id: str, conversation_id: str, is_new_conversation: bool) -> None:
        conversation = await self.highrise.get_messages(conversation_id)
        message = conversation.messages[0].content
        response = await self.command_handler(user_id, message)
        if response:
            try:
                await self.highrise.send_message(conversation_id, response)
            except Exception as e:
                print(f"Messaging Error: {e}")

    # Handle commands from any source (chat/whisper/message)

    async def command_command(self, user: User, message: str):
        parts = message.split(" ")
        command = parts[0][1:]
        functions_folder = "commande"
        for file_name in os.listdir(functions_folder):
            if file_name.endswith(".py"):
                module_name = file_name[:-3] 
                module_path = os.path.join(functions_folder, file_name)
                    
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                    
                    
                if hasattr(module, command) and callable(getattr(module, command)):
                    function = getattr(module, command)
                    await function(self, user, message)

    async def command_moderation(self, user: User, message: str):
        parts = message.split(" ")
        command = parts[0][1:]
        functions_folder = "moderation"
        for file_name in os.listdir(functions_folder):
            if file_name.endswith(".py"):
                module_name = file_name[:-3] 
                module_path = os.path.join(functions_folder, file_name)
                    
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                    
                    
                if hasattr(module, command) and callable(getattr(module, command)):
                    function = getattr(module, command)
                    await function(self, user, message)

    async def command_outfit(self, user: User, message: str):
            parts = message.split(" ")
            command = parts[0][1:]
            functions_folder = "outfit"
            for file_name in os.listdir(functions_folder):
                if file_name.endswith(".py"):
                    module_name = file_name[:-3] 
                    module_path = os.path.join(functions_folder, file_name)
                    
                    spec = importlib.util.spec_from_file_location(module_name, module_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    
                    
                    if hasattr(module, command) and callable(getattr(module, command)):
                        function = getattr(module, command)
                        await function(self, user, message)

    async def command_game(self, user: User, message: str):
        parts = message.split(" ")
        command = parts[0][1:]
        functions_folder = "game"
        for file_name in os.listdir(functions_folder):
            if file_name.endswith(".py"):
                module_name = file_name[:-3] 
                module_path = os.path.join(functions_folder, file_name)
                    
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                    
                # Check if the function exists in the module
                if hasattr(module, command) and callable(getattr(module, command)):
                    function = getattr(module, command)
                    await function(self, user, message)

    async def command_handler(self, user_id, message: str):
        if user_id != self.owner_id:  # Only listen to host's commands
            return
        command = message.lower().strip()

        if command.startswith("!set"): # Set the bot at your location
            set_position = await self.set_bot_position(user_id)
            return set_position
        elif command.startswith("!top"): # Build a 10 top tippers leaderboard
            top_tippers = self.get_top_tippers()
            formatted_tippers = []
            for i, (user_id, user_data) in enumerate(top_tippers):
                username = user_data['username']
                total_tips = user_data['total_tips']
                formatted_tippers.append(f"{i + 1}. {username} ({total_tips}g)")

            tipper_message = '\n'.join(formatted_tippers)
            return f"Top Tippers:\n{tipper_message}"
        elif command.startswith("!get "): # Query a specific user's tips
            username = command.split(" ", 1)[1].replace("@", "")
            tip_amount = self.get_user_tip_amount(username)
            if tip_amount is not None:
                return f"{username} has tipped {tip_amount}g"
            else:
                return f"{username} hasn't tipped."
        elif command.startswith("!wallet"): # Get Bot wallet gold
            wallet = await self.highrise.get_wallet()
            for currency in wallet.content:
                if currency.type == 'gold':
                    gold = currency.amount
                    return f"I have {gold}g in my wallet."
            return "No gold in wallet."

    async def on_tip(
        self, sender: User, receiver: User, tip: CurrencyItem | Item
    ) -> None:
        if isinstance(tip, CurrencyItem):
            print(f"{sender.username} tipped {tip.amount}g -> {receiver.username}")
            if receiver.id == self.bot_id:
                if sender.id not in self.tip_data:
                    self.tip_data[sender.id] = {"username": sender.username, "total_tips": 0}

                self.tip_data[sender.id]['total_tips'] += tip.amount
                self.write_tip_data(sender, tip.amount)

                if tip.amount >= 500:
                    await self.highrise.chat(f"Thank you {sender.username} for the generous {tip.amount}g tip!")

    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        print(f"{user.username} joined the room")

    async def on_user_leave(self, user: User) -> None:
        print(f"{user.username} left the room")

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print(f"🟢 - Bot en ligne dans SkyClub \n version du bot [{botconfig.version} {botconfig.versionvaleur}] mise a jour le {botconfig.lastmaj} \n©️ FRVNCHE INDUSTRY")
        self.bot_id = session_metadata.user_id
        self.owner_id = session_metadata.room_info.owner_id
        if self.bot_status:
            await self.place_bot()
        self.bot_status = True

    def get_top_tippers(self):
        sorted_tippers = sorted(self.tip_data.items(), key=lambda x: x[1]['total_tips'], reverse=True)
        return sorted_tippers[:10]

    # Return the amount a particular username has tipped
    def get_user_tip_amount(self, username):
        for _, user_data in self.tip_data.items():
            if user_data['username'].lower() == username.lower():
                return user_data['total_tips']
        return None

    # Place bot on start
    async def place_bot(self):
        while self.bot_status is False:
            await asyncio.sleep(0.5)
        try:
            self.bot_position = self.get_bot_position()
            if self.bot_position != Position(0, 0, 0, 'FrontRight'):
                await self.highrise.teleport(self.bot_id, self.bot_position)
                return
        except Exception as e:
            print(f"Error with starting position {e}")

    # Write tip event to file
    def write_tip_data(self, user: User, tip: int) -> None:
        with open("./data.json", "r+") as file:
            data = load(file)
            file.seek(0)
            user_data = data["users"].get(user.id, {"total_tips": 0, "username": user.username})
            user_data["total_tips"] += tip
            user_data["username"] = user.username
            data["users"][user.id] = user_data
            dump(data, file)
            file.truncate()

    # Set the bot position at player's location permanently
    async def set_bot_position(self, user_id) -> None:
        position = None
        try:
            room_users = await self.highrise.get_room_users()
            for room_user, pos in room_users.content:
                if user_id == room_user.id:
                    if isinstance(pos, Position):
                        position = pos

            if position is not None:
                with open("./data.json", "r+") as file:
                    data = load(file)
                    file.seek(0)
                    data["bot_position"] = {
                        "x": position.x,
                        "y": position.y,
                        "z": position.z,
                        "facing": position.facing
                    }
                    dump(data, file)
                    file.truncate()
                set_position = Position(position.x, (position.y + 0.0000001), position.z, facing=position.facing)
                await self.highrise.teleport(self.bot_id, set_position)
                await self.highrise.teleport(self.bot_id, position)
                await self.highrise.walk_to(position)
                return "Updated bot position."
            else:
                return "Failed to update bot position."
        except Exception as e:
            print(f"Error setting bot position: {e}")

    # Load tip data on start
    def load_tip_data(self) -> None:
        with open("./data.json", "r") as file:
            data = load(file)
            self.tip_data = data["users"]

    # Load bot position from file
    def get_bot_position(self) -> Position:
        with open("./data.json", "r") as file:
            data = load(file)
            pos_data = data["bot_position"]
            return Position(pos_data["x"], pos_data["y"], pos_data["z"], pos_data["facing"])

    async def run_bot(self, room_id, api_key) -> None:
        asyncio.create_task(self.place_bot())
        definitions = [BotDefinition(self, room_id, api_key)]
        await __main__.main(definitions)

# Automatically create json file if not exists
def data_file(filename: str, default_data: str = "{}") -> None:
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write(default_data)

DEFAULT_DATA = '{"users": {}, "bot_position": {"x": 0, "y": 0, "z": 0, "facing": "FrontRight"}}'
data_file("./data.json", DEFAULT_DATA)

if __name__ == "__main__":
    arun(Bot().run_bot(room_id, api_key))
