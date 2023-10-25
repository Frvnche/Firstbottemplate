from highrise import *
from highrise.webapi import *
from highrise.models_webapi import *
from highrise.models import *


async def wallet(self, user: User, message: str) -> None:
    wallet = await self.highrise.get_wallet()
    for currency in wallet.content:
        if currency.type == 'gold':
            gold = currency.amount
            if gold == 0:
                await self.highrise.chat(f"je n'ai pas d'or pour l'instant")
            elif gold <= 50:
                await self.highrise.chat(f"j'ai {gold}g dans ma poche")
            elif gold <= 100:
                await self.highrise.chat(f"j'ai {gold}g dans mon porte-feuille")
            elif gold <= 500:
                await self.highrise.chat(f"j'ai {gold}g dans mon sac")
            else:
                await self.highrise.chat(f"j'ai {gold}g dans mon compte en banque.")
    