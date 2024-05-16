import enemy
import player_item 
import random
import json

def load_enemies():
    with open('enemies.json', 'r') as f:
        enemy_stats = json.load(f)

    enemies = []

    for enemy_stat in enemy_stats:
        enemies.append(
                enemy.Enemy(
                    enemy_stat["Name"],
                    enemy_stat["HP"],
                    enemy_stat["Damage"],
                    enemy_stat["Type"]
                    )
                )
        
    return enemies

def load_inventory():
    with open('items.json', 'r') as f:
        inventory = json.load(f)

    items = []

    for item in inventory:
        items.append(
                player_item.PlayerItem(
                    item["Name"],
                    item["Damage"],
                    item["Good Type"],
                    item["Bad Type"]
                    )
                )

    return items

def spawn_enemies():
    num_enemies = random.randint(1, 2)
    enemies = []
    enemy_data = load_enemies()
    for _ in range(num_enemies):
        enemy = random.choice(enemy_data)
        enemies.append(enemy)
    return enemies

def display_attacks(inventory_items):
    print("Available Attacks:")
    for i, item in enumerate(inventory_items):
        print(f"{i+1}: {item.name} - Damage: {item.damage} - Good Type: {item.good_type} - Bad Type: {item.bad_type}")

def display_enemies(enemies):
    print("Enemies:")
    for i, enemy in enumerate(enemies):
        print(f"{i+1}: {enemy.name} - HP: {enemy.hp} - Damage: {enemy.damage} - Type: {enemy.enemy_type}")

def welcome(waves):
    print("**************************")
    print("Welcome to the game!")
    print(f"You will be fighting {waves} waves of enemies.")
    print("**************************")
    print()
    input("Press Enter to continue...")

def main():
    player_hp = 100
    enemies = spawn_enemies()
    waves = random.randint(1, 3) # 1-3 waves of enemies

    welcome(waves)

    while True:
        if not enemies:
            if waves > 0:
                enemies = spawn_enemies()
                waves -= 1
            else:
                print("You win!")
                break

        print("\n**************************\n")

        display_enemies(enemies)

        inventory_items = load_inventory()
        display_attacks(inventory_items)

        try:
            enemy_choice = input("\nChoose an enemy to attack (1-{}): ".format(len(enemies)))
            enemy_choice = int(enemy_choice)
            enemy = enemies[enemy_choice - 1]
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid number.")
            continue

        try:
            item_choice = input("\nChoose an item to attack with (1-{}): ".format(len(inventory_items)))
            item_choice = int(item_choice)
            item = inventory_items[item_choice- 1]
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid number.")
            continue
        

        if enemy.enemy_type == item.good_type:
            enemy.hp -= item.damage * 2
            print(f"Super effective! You dealt {item.damage * 2} damage to {enemy.name}.")
        elif enemy.enemy_type == item.bad_type:
            enemy.hp -= item.damage // 2
            print(f"Not effective... You dealt {item.damage // 2} damage to {enemy.name}.")
        else:
            enemy.hp -= item.damage
            print(f"You dealt {item.damage} damage to {enemy.name}.")

        if enemy.hp <= 0:
            print(f"You killed {enemy.name}!")
            enemies.remove(enemy)

        if not enemies:
            print("You win!")
            break

        for enemy in enemies:
            print(f"{enemy.name} attacks you for {enemy.attack()} damage.")
            player_hp -= enemy.attack()

        if player_hp <= 0:
            print("You lose!")
            break

        print(f"You have {player_hp} HP left.")

        print()

        input("Press Enter to continue...")

if __name__ == "__main__":
    main()

