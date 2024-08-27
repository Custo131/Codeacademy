inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]
#length of inventory
inventory_len = len(inventory)
#First item 
first = inventory[0]
#last inventory 
last = inventory[-1]

#inventory_2_6 
inventory_2_6 = inventory[2:6]
#first 3 
first_3 = inventory[0:3]


# How many twin beds
twin_beds = inventory.count("twin bed")

#removed items 
removed_item = inventory.pop(4)
# insert new items
inventory.insert(10,"19th Century Bed Frame")

sorted_list = sorted(inventory)
inventory = sorted_list