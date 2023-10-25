from highrise import *
from highrise.webapi import *
from highrise.models_webapi import *
from highrise.models import *
from config.config import botconfig


async def help(self, user: User, message: str) -> None:
    if user.username in botconfig.ownername:
            await self.highrise.chat(f"salut {user.username} vous posséder la permission Owner")
            pass
    elif user.username in botconfig.moderateur:
           await self.highrise.chat(f"salut {user.username} vous posséder la permission Modérateur")
           pass
    elif user.username in botconfig.contributeur:
            await self.highrise.chat(f"salut {user.username} vous posséder la permission contributeur")
            pass
    else:
            await self.highrise.chat(f"désolée {user.username} !vous n'avez aucune permissions !")
            pass
    
    await self.highrise.chat(f"'s pannel \nListe de commande Utile 🔰\n{botconfig.prefix}help      | Affiche les commande d'aide\n{botconfig.prefix}wallet   | Affiche le porte feuille du bot\n{botconfig.prefix}info       | info sur les roles")
    await self.highrise.chat(f"'s pannel \nListe de commande modération 🛡️\n{botconfig.prefix}kick      |expulse un utilisateur\n{botconfig.prefix}equip   | change l'apparence du bot")
    await self.highrise.chat(f"'s Premium Pannel \n Commande Premium \n{botconfig.prefix}tpto | se teleporter a un joueur \n{botconfig.prefix}follow | le bot vous suit ! \n{botconfig.prefix}teleport | teleporter un joueur a des coordonée")
    print (f"[CMD] help by {user.username}")