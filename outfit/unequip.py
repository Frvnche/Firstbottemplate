from highrise import *
from highrise.models import *

categories = ["aura","bag","blush","body","dress","earrings","emote","eye","eyebrow","fishing_rod","freckle","fullsuit","glasses",
"gloves","hair_back","hair_front","handbag","hat","jacket","lashes","mole","mouth","necklace","nose","rod","shirt","shoes",
"shorts","skirt","sock","tattoo","watch"]

async def unequip(self: BaseBot, user: User, message: str):
        parts = message.split(" ")
        if len(parts) != 2:
            await self.highrise.chat("Invalid command format. You need to specify the category.")
            return
        if parts[1] not in categories:
            await self.highrise.chat("Invalid category.")
            return
        category = parts[1].lower()
        outfit = (await self.highrise.get_my_outfit()).outfit
        for outfit_item in outfit:
            #the category of the item in an outfit can be found by the first string in the id before the "-" character
            item_category = outfit_item.id.split("-")[0][0:3]
            if item_category == category[0:3]:
                try:
                    outfit.remove(outfit_item)
                except:
                    await self.highrise.chat(f"The bot isn't using any item from the category '{category}'.")
                    return
        response = await self.highrise.set_outfit(outfit)
        print(response)