def welcome():
    print("Welcome to the Fantasy Shop!")
    print("You have 100 gold and an empty inventory.\n")

def display_shop(shop):
    print("Shop Items:")
    for item, price in shop.items():
        print(f"{item}: {price} gold")

def display_inventory(inventory, gold):
    print("\nYour Inventory:")
    for item in inventory:
        print(item)
    print(f"Remaining Gold: {gold}\n")

def main():
    shop = {"potion": 10, "rope": 10, "knife": 20, "locket": 30, "shield": 30, "sword": 50, "armor": 60, "wand": 60, "staff": 80, "grimoire": 90}
    inventory = []
    gold = 100
    game_run = True

    welcome()

    while game_run:
        display_shop(shop)
        print("\nCommands: 'buy item', 'sell item', 'inventory', 'exit'")
        choice = input("\nEnter your command: ").lower().split()

        if choice[0] == "exit":
            game_run = False
        elif choice[0] == "buy" and len(choice) > 1:
            item = ' '.join(choice[1:])
            if item in shop:
                if gold >= shop[item]:
                    gold -= shop[item]
                    inventory.append(item)
                    print(f"You bought a {item}.")
                else:
                    print("You don't have enough gold to buy that.")
            else:
                print("Item not found in shop.")
        elif choice[0] == "sell" and len(choice) > 1:
            item = ' '.join(choice[1:])
            if item in inventory:
                gold += shop[item] // 2
                inventory.remove(item)
                print(f"You sold a {item} for {shop[item] // 2} gold.")
            else:
                print("Item not found in your inventory.")
        elif choice[0] == "inventory":
            display_inventory(inventory, gold)
        else:
            print("Invalid command.")

        print("\n")

    print("Thanks for shopping! Here's your final inventory:")
    display_inventory(inventory, gold)

if __name__ == "__main__":
    main()