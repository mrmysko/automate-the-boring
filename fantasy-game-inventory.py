def displayInventory(inventory: dict):

    print("Inventory:")
    for key, value in inventory.items():
        print(value, key)
    print(f"Total number of items: {sum(inventory.values())}")


def addToInventory(inventory: dict, loot: list) -> dict:

    for i in loot:
        if i not in inventory:
            inventory.setdefault(i, 1)
        else:
            inventory[i] += 1

    return inventory


def main():

    inventory = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
    displayInventory(inventory)

    loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
    addToInventory(inventory, loot)

    displayInventory(inventory)


if __name__ == "__main__":
    main()
