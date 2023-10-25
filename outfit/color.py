from highrise import *
from highrise.models import *

async def color(self: BaseBot, user: User, message: str):
        parts = message.split(" ")
        print (parts)
        if len(parts) != 3:
            await self.highrise.chat("Invalid command format. You need to specify the category and color palette number.")
            return
        category = parts[1]
        try:
            color_palette = int(parts[2])
        except:
            await self.highrise.chat("Invalid command format. You need to specify the category and color palette number.")
            return
        outfit = (await self.highrise.get_my_outfit()).outfit
        for outfit_item in outfit:
            #the category of the item in an outfit can be found by the first string in the id before the "-" character
            item_category = outfit_item.id.split("-")[0]
            if item_category == category:
                try:
                    outfit_item.active_palette = color_palette
                except:
                    await self.highrise.chat(f"The bot isn't using any item from the category '{category}'.")
                    return
        await self.highrise.set_outfit(outfit)