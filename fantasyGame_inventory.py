
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    """
    Displays the inventory of items within the dictionary
    """
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total = item_total + inventory.get(k, 0)
    
    print("Total number of items: " + str(item_total))

displayInventory(stuff)
print()

def addToInventory(inventory, addedItems):
    """
    Adds item count/items to a dictionary
    """
    for item in addedItems:
        # if item does not exist
        if item not in inventory.keys():
            inventory[item] = 1
        else:
            # if item exists
            inventory[item] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)