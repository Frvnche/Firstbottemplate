from highrise import *
from highrise.webapi import *
from highrise.models_webapi import *
from highrise.models import *
from config.config import botconfig


async def info(self, user : User, message : str ):
    if user.username in botconfig.ownername:
            await self.highrise.chat(f"l'owner devrait savoir ca mais un petit rapelle ca fait du bien")
            pass
    elif user.username in botconfig.moderateur:
            await self.highrise.chat(f"vous disposez d'une permission moderation")
            pass
    elif user.username in botconfig.contributeur:
            await self.highrise.chat(f"vous disposez deja de la permission contributeur")
            pass
    else:
           await self.highrise.chat(f"Pour disposer de permission suplémentaire et ainsi utilisé les commande premium voici les quelques etapes ⬇️")
           pass
    
    await self.highrise.chat(f"{botconfig.botname} contient un système spécifique d'autorisations automatique qui se met a jour automatiquement \n \nvoici la hiérarchie")
    await self.highrise.chat(f"💎 VIP +                | don 1K ou +\n🪙 VIP                   | don 500golds ou + \n 🎟️ contributeur | don 50golds")
    await self.highrise.chat(f"\n ses roles vous permettrons d'acceder a des permission différente comme la télèportation et les nouvelle commande en avance!")
    print (f"[CMD] info by {user.username}")