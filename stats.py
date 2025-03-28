import random, time, sys, os
from text_custom import to_color


stat_info = {"Health": 10, "Strength": 0, "Luck": 0, "Charm": 0}

class character:
    def __init__(self, name, health, strength, luck, charm, stamina):
        self.health = health
        self.strength = strength
        self.luck = luck
        self.charm = charm
        self.name = name
        self.stamina = stamina

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0 and self.stamina > 0

    def attack(self, enemy):
        damage = self.strength + random.randint(0, self.luck)
        enemy.take_damage(damage)
        print(f"{self.name} hit {enemy.name} for {damage} damage.")

    def allocate_stats(self, points):
        while points > 0:
            print(to_color(f"You have {points} points left", 'red'))
            print(to_color(f"Health: {self.health}, Strength: {self.strength}, Luck: {self.luck}, Charm: {self.charm}, Stamina: {self.stamina}", 'yellow'))

            stat_choice = input("Which stat would you like to increase? \n(Health, Strength, Luck, Charm, or Stamina?): ")

            stat_choice = stat_choice.title()

            if stat_choice not in ['Health', 'Strength', 'Luck', 'Charm', 'Stamina']:
                print("Invalid choice... Try again!")
            else:
                while True:
                    amount = input(f"How many points do you want to add to {stat_choice}? ")

                    if amount.isdigit():
                        amount = int(amount)
                        if 0 <= amount <= points:
                            if stat_choice == "Health":
                                self.health += amount
                            elif stat_choice == "Strength":
                                self.strength += amount
                            elif stat_choice == "Luck":
                                self.luck += amount
                            elif stat_choice == "Charm":
                                self.charm += amount
                            elif stat_choice == 'Stamina':
                                self.stamina += amount

                            points -= amount
                            break
                        else:
                            print(f"Invalid amount. You can only add up to {points} points.")
                    else:
                        print("Please enter a valid number (digits only).")


    def randomize_stats(self):
        self.health = random.randint(8, 12)
        self.luck = random.randint(3, 8)
        self.charm = random.randint(2, 6)
        self.strength = random.randint(3, 8)
        self.stamina = random.randint(15, 20)

    def print_stats(self):
        print("\nYour stats are: ")
        print(to_color(f"Health: {self.health}, Strength: {self.strength}, Luck: {self.luck}, Charm: {self.charm}, Stamina: {self.stamina}", 'yellow'))

    def remove_stat(self, stat, amount):
        if stat == "health":
            if self.health > amount:
                self.health -= amount
            else:
                self.health = 0
            print(f"Lost {amount} Health. New Health: {self.health}")

        elif stat == "strength":
            if self.strength > amount:
                self.strength -= amount
            else:
                self.strength = 0
            print(f"Lost {amount} Strength. New Strength: {self.strength}")

        elif stat == "luck":
            if self.luck > amount:
                self.luck -= amount
            else:
                self.luck = 0
            print(f"Lost {amount} Luck. New Luck: {self.luck}")

        elif stat == "charm":
            if self.charm > amount:
                self.charm -= amount
            else:
                self.charm = 0
            print(f"Lost {amount} Charm. New Charm: {self.charm}")
        elif stat == "stamina":
            if self.stamina > amount:
                self.stamina -= amount
            else:
                self.stamina = 0
            print(f"Lost {amount} Stamina. New Stamina: {self.stamina}")
        else:
            print('bruh moment fr')


##########-ATTACKING FUNCTIONS##########
def normal_attack(player, enemy):
    if player.stamina >= 2:

        damage = player.strength
        enemy.take_damage(damage)
        print(to_color(f"{player.name} used Normal Attack! {enemy.name} took {damage} damage.", 'blue'))
        print(to_color(f"{player.name} used up 2 stamina!", 'blue'))
        player.stamina -= 2
        print(to_color(f"you lost 2 stamina", 'yellow'))

    else:
        print('not enough stamina, your atack failed')

def power_attack(player, enemy):
    if player.stamina >= 5:
        damage = player.strength + random.randint(3, 5)
        enemy.take_damage(damage)
        print(to_color(f"{player.name} used Power Attack! {enemy.name} took {damage} damage!", 'blue'))
        print(to_color(f"{player.name} used up 5 stamina!", 'blue'))
        player.stamina -= 5
        print(to_color(f"you lost 5 stamina", 'yellow'))

    else:
        print("not enough stamina, your atack failed")

def heal(player, _):
    if player.stamina >= 1:
        heal_amount = random.randint(2, 5)
        player.health += heal_amount
        print(to_color(f"{player.name} healed for {heal_amount} HP!", 'blue'))
        print(to_color(f"{player.name} used up 1 stamina", 'blue'))
        player.stamina -= 1
        print(to_color(f"you lost 1 stamina", 'yellow'))
    else:
        print("not enough stamina, your heal failed")

# List for the attacks
attack_moves = [normal_attack, power_attack, heal]


##########BATTLE SYSTEM##########
def player_turn(player, enemy):


    print("\nChoose an attack:")
    print("1. Normal Attack(2 stamina)")
    print("2. Power Attack(5 stamina)")
    print("3. Heal(1 stamina)")

    while True:
        choice = input("Enter the number of your move: ")
        if choice in ["1", "2", "3"]:
            move_index = int(choice) - 1
            attack_moves[move_index](player, enemy)
            break
        else:
            print("Bruh, that's not a valid move. Try again!")

    if not player.is_alive():
        print(f"{player.name} has fallen! {enemy.name} wins!")
        time.sleep(1)
        return False
    return True

def enemy_turn(player, enemy):
    move_index = random.randint(0, 2)
    attack_moves[move_index](enemy, player)
    print(to_color(f"{enemy.name} made their move!", 'red'))
    time.sleep(1)

    if not enemy.is_alive():
        print(f"{enemy.name} has fallen! {player.name} wins!")
        time.sleep(1)
        return False
    return True

def battle(player, enemy):
    print("Battling Time!")
    time.sleep(1)
    player.print_stats()
    print(f'{enemy.name}s Stats are:')
    print(to_color(f"Health: {enemy.health}, Strength: {enemy.strength}, Luck: {enemy.luck}, Charm: {enemy.charm}, Stamina: {enemy.stamina}", 'yellow'))


    while player.is_alive() and enemy.is_alive():
        # Player's turn
        if not player_turn(player, enemy):
            break

        time.sleep(1)

        if not enemy.is_alive():
            break  # Exit if enemy is dead

        # Enemy's turn
        if not enemy_turn(player, enemy):
            break

        time.sleep(1)

        if not player.is_alive():
            break  # Exit if player is dead

        # Show stats for both player and enemy
        player.print_stats()
        print(f'{enemy.name}s Stats are:')
        print(to_color(f"Health: {enemy.health}, Strength: {enemy.strength}, Luck: {enemy.luck}, Charm: {enemy.charm}, Stamina: {enemy.stamina}", 'yellow'))

        print('------------------------------------------------------------------')
        time.sleep(1)

    # If player is alive, the player won
    if player.is_alive():
        print(f"{player.name} wins the battle!")
        time.sleep(1)
        return True  # Player wins
    else:
        print(f"{enemy.name} wins the battle!")
        time.sleep(1)
        return False  # Player loses

#########-CREATE CHARACTER-#########
def create_character(health=10, stamina=20):
    print("It's time to make your character!")
    character_name = input("Enter your name: ")
    points = 10
    randomize_or_not = input("Do you want to randomize your stats? If so type 'Y': ")
    randomize_or_not = randomize_or_not.title()
    player = character(character_name, health, 2, 2, 2, stamina)

    if randomize_or_not == "Y":
        player.randomize_stats()
    else:
        player.allocate_stats(points)

    player.print_stats()
    return player
