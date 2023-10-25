from highrise import *
from highrise.webapi import *
from highrise.models_webapi import *
from highrise.models import *

async def equip(self: BaseBot, user: User, message: str):
        #gets the item id and category from the message
        parts = message.split(" ")
        if len(parts) < 2:
            await self.highrise.chat("You need to specify the item name.")
            return
        item_name = ""
        for part in parts[1:]:
            item_name += part + " "
        item_name = item_name[:-1]
        #check if the last part of the message is a number
        index = 0
        if item_name[-1].isdigit():
            item_name = item_name[:-2]
            index = int(parts[-1])
        item = (await self.webapi.get_items(item_name = item_name)).items
        #checks if the response is valid
        if item == []:
            await self.highrise.chat(f"Item '{item_name}' not found.")
            return
        elif len(item) > 1:
            await self.highrise.chat(f"Multiple items found for '{item_name}', using the item number {index} in the list {item[index].item_name}.")
        item = item[index]
        item_id = item.item_id
        category = item.category
        #--------------------------------------------------------#
        
        verification = False
        #checks if the bot has the item
        inventory = (await self.highrise.get_inventory()).items
        for inventory_item in inventory:
            if inventory_item.id == item_id:
                verification = True
                break
        if verification == False:
            #checks if the item is free
            if item.rarity == Rarity.NONE:
                pass
            #checks if the item is purchasable
            elif item.is_purchasable == False:
                await self.highrise.chat(f"Item '{item_name}' can't be purchased.")
                return
            else:
                try:
                    response = await self.highrise.buy_item(item_id)
                    if response != "success":
                        await self.highrise.chat(f"Item '{item_name}' can't be purchased.")
                        return
                    else:
                        await self.highrise.chat(f"Item '{item_name}' purchased.")
                except Exception as e:
                    print(e)
                    await self.highrise.chat(f"Exception: {e}'.")
                    return
                
        #--------------------------------------------------------#
        new_item = Item(type = "clothing",
                    amount = 1,
                    id = item_id, 
                    account_bound=False,
                    active_palette=0,)
        #--------------------------------------------------------#
        #checks if the item category is already in use
        outfit = (await self.highrise.get_my_outfit()).outfit
        items_to_remove = []
        for outfit_item in outfit:
            #the category of the item in an outfit can be found by the first string in the id before the "-" character
            item_category = outfit_item.id.split("-")[0][0:4]
            print(f"{item_category}")
            if item_category == category[0:4]:
                items_to_remove.append(outfit_item)
        for item_to_remove in items_to_remove:
            outfit.remove(item_to_remove)
        #if the item is a hair, also equips the hair_back
        if category == "hair_front":
            hair_back_id = item.link_ids[0]
            hair_back = Item(type = "clothing",
                            amount = 1,
                            id = hair_back_id, 
                            account_bound=False,
                            active_palette=0,)
            outfit.append(hair_back)
        outfit.append(new_item)
        await self.highrise.set_outfit(outfit)