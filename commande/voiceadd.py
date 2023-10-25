from highrise import *
from highrise.models import *
from config.config import botconfig

async def voiceadd(self, user: User, message: str) -> None:
    if message.lower().startswith("/voiceadd "):
            try:
                command, username = message.split(" ")
            except:
                await self.highrise.chat("Invalid command, please use /voiceadd <username>")
                return
            #gets room users and check if the user is in the room
            room_users = (await self.highrise.get_room_users()).content
            for room_user, position in room_users:
                if room_user.username.lower() == username.lower():
                    user_id = room_user.id
                    break
            if "user_id" not in locals():
                await self.highrise.chat(f"l'utilisateur '{username}' n'a pas etait trouvée.")
                return
				
            #checks if the user is already in the voice list
            voice_list = (await self.highrise.get_voice_status()).users
            if user_id in voice_list:
                await self.highrise.chat(f"l'utilisateur {username} posséde déja le micro")
                return
				    
            await self.highrise.add_user_to_voice(user_id)
            await self.highrise.chat(f"j'ai ajouté @{username} au vocale.")
            print (f"[CMD] voiceadd by {user.username} for @{username}")