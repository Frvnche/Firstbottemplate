from highrise import *
from highrise.webapi import *
from highrise.models_webapi import *
from highrise.models import *
from config.config import botconfig

async def tip(self, user: User, message: str) -> None:
    if user.username in botconfig.ownername:
        pass
    else:
        await self.highrise.chat("vous n'avez pas la permission requise pour cette commande")
        return
    parts = message.split(" ")
    if len(parts) != 2:
        await self.highrise.send_message(user.id, "commande invalide")
        return
    #checks if the amount is valid
    try:
        amount = int(parts[1])
    except:
        await self.highrise.chat("montant invalide")
        return
    #checks if the bot has the amount
    bot_wallet = await self.highrise.get_wallet()
    bot_amount = bot_wallet.content[0].amount
    if bot_amount <= amount:
        await self.highrise.chat("les frais ne me permettent pas de tips ce prix")
        return
    bars_dictionary = {10000: "gold_bar_10k", 
                        5000: "gold_bar_5000",
                        1000: "gold_bar_1k",
                        500: "gold_bar_500",
                        100: "gold_bar_100",
                        50: "gold_bar_50",
                        10: "gold_bar_10",
                        5: "gold_bar_5",
                        1: "gold_bar_1"}
    fees_dictionary = {10000: 1000,
                        5000: 500,
                        1000: 100,
                        500: 50,
                        100: 10,
                        50: 5,
                        10: 1,
                        5: 1,
                        1: 1}
    #loop to check the highest bar that can be used and the amount of it needed
    tip = []
    total = 0
    for bar in bars_dictionary:
        if amount >= bar:
            bar_amount = amount // bar
            amount = amount % bar
            for i in range(bar_amount):
                tip.append(bars_dictionary[bar])
                total = bar+fees_dictionary[bar]
    if total > bot_amount:
        await self.highrise.chat("pas assez dans le portefeuille")
        return
    for bar in tip:
        await self.highrise.tip_user(user.id, bar)
        wallet = (await self.highrise.get_wallet()).content
        print (f"[CMD MOD] tip by {user.username} nouveaux montant : {wallet[0].amount}")
