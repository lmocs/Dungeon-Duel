# dungeon game 
# player has three lives (3 characters)
# enemies behind a door
# rock paper scissors fight
    # or 007 logic
    # shoot reload block
# three doors assigned 1,2,3-6 randint
# 1 is safe, 2 is a monster, 3 is a heal, 4 is a shop
# after killing a monster, random chance to gain 1 coin

    # ENDED AT THE SHOP !!!

    # with coins you can purchase magic power that insta-kills monsters
    # perks that increase the chance of dropping coins or finding safe havens
    # gain a life
# score counter
# door counter

# Problems:
# I did this project and i learned more about nested loops 
# idk that i needed continue instead of return
# Continue only when i want to move on
# I didnt know that once the object was dead, i had to remove it from the monster_list

import random

class Character:

    def __init__(self, name, weapon, lives, coins):
        self.name = name
        self.weapon = weapon
        self.lives = lives
        self.coins = coins

    def battle(self):
        ammo = 1
        random_coins = random.randint(0, 3)
        opponent = random.choice(monster_list)
        opponent_moves = ['s', 'd', 'r']

            # add attack names


        while self.lives > 0 and opponent.life == 1:
            monster_move = random.choice(opponent_moves)

            move = str(input(f"\nYou encountered a {opponent.name}! Shoot ('s'), dodge ('d'), or reload ('r'): "))

            # This prevents the player from shooting when they have no ammo
            if ammo == 0:
                if move == 's' and monster_move == 's':
                    self.lives -= 1
                    print(f"The {opponent.name} killed you while you tried to shoot your {self.weapon} with no ammo!")
                    print(f"You have {self.lives} lives left. ")
                
                if move == 's' and monster_move == 'd':
                    print(f"The {opponent.name} dodged your {self.weapon} with no ammo! Now both of you look dumb. ")
                
                if move == 's' and monster_move == 'r':
                    print(f"The {opponent.name} laughed at your dumbass for shooting a {self.weapon} with no ammo! Humiliating! ")

            # This allows the player to reload or dodge whether they have ammo or not 
            if ammo >= 1 or move == 'r' or move == 'd':
                if move == 's' and monster_move == 's':
                    ammo -= 1
                    self.lives -= 1
                    opponent.life -= 1
                    self.coins += random_coins
                    print(f"You and the {opponent.name} killed each other. You gained {self.coins} coin(s) from defeating the {opponent.name}.")
                    print(f"You have {self.lives} lives left and {self.coins} coin(s) total. ")
                    monster_list.remove(opponent)
                    continue

                elif move == 's' and monster_move == 'd':
                    ammo -= 1
                    print(f"You shot, but the {opponent.name} dodged! Ammo: {ammo}") 

                elif move == 's' and monster_move == 'r':
                    ammo -= 1
                    opponent.life -= 1
                    self.coins += random_coins
                    print(f"You shot the {opponent.name} dead. You gained {self.coins} coin(s) from defeating the {opponent.name}. ")
                    print(f"You have {self.lives} lives left and {self.coins} coin(s) total. ")
                    monster_list.remove(opponent)
                    continue

                elif move == 'd' and monster_move == 'd':
                    print(f"Both you and the {opponent.name} dodged! ")

                elif move == 'd' and monster_move == 's':
                    print(f"You dodged the {opponent.name}'s attack! ")

                elif move == 'd' and monster_move == 'r':
                    print(f"You dodged, but the {opponent.name} taunted at you! ")

                elif move == 'r' and monster_move == 'r':
                    ammo += 1
                    print(f"While you were busy reloading, the {opponent.name} taunted you! Ammo: {ammo}")

                elif move == 'r' and monster_move == 's':
                    self.lives -= 1
                    ammo += 1
                    print(f"The {opponent.name} killed you while you were reloading. You have {self.lives} lives left. Ammo: {ammo}")

                elif move == 'r' and monster_move == 'd':
                    ammo += 1
                    print(f"You reloaded your gun while the {opponent.name} looked stupid and dodged nothing! How embarrassing! Ammo: {ammo}")

    def shop(self):

        pass

    def game(self):
        # The game starts at level 1
        level = 1
        print(f"\nYou begin your journey on level {level}. ")
        # The game ends when level 10 is reached
        while level < 10:
            # 'path' prompts the user to pick a direction to go
            path = str(input("\nThere are three doors. Go left ('l'), right ('r'), or straight ('s'): "))

            # Each 'path' is the same, regardless of the direction
            if path == 'l' or path == 'r' or path == 's':
                # I made the range(1, 8) so that there is a 3/8 chance of safety and 5/8 chance to battle. 
                door = random.randint(1, 8)

                if door == 1:
                    level += 1
                    print(f"You found a safe haven! Continue onwards. You are now on level {level}. ")
                    continue

                elif door == 2:
                    self.lives += 1
                    level += 1
                    print(f"You gained a life, you now have {self.lives} lives. You are now on level {level}. ")
                    continue

                elif door == 3:
                    print("Shop")
                    continue

                else:
                    p1.battle()
                    if self.lives == 0:
                        print(f"You died on level {level}. Game over! ")
                        exit()
                    level += 1
                    print(f"Congratulations, you are now on level {level}. ")
                    continue

class Monster:

    def __init__(self, name, attack, life):
        self.name = name
        self.attack = attack
        self.life = life

# class Door:

# want to find a better way to define objects in a list

p1 = Character("Ed", "Gun", 3, 0)

p2 = Character("Edd", "Gun", 1, 0)
p3 = Character("Eddy", "Gun", 1, 0)

m1 = Monster("Demon", "Claw", 1)
m2 = Monster("Ogre", "Club", 1)
m3 = Monster("Dragon", "Flamethrower", 1)
m4 = Monster("Skeleton", "Bone", 1)
m5 = Monster("Werewolf", "Bite", 1)

monster_list = []

monster_list.append(m1)
monster_list.append(m2)
monster_list.append(m3)
monster_list.append(m4)
monster_list.append(m5)



# This is the intro to the game!
print("\nWelcome to Dungeon Duel!")
start = str(input("Type 'r' if you're ready or 'y' if you would like to read the tutorial: "))

if start == 'y':
    print("\nYour mission is to make it out alive from the dungeon of monsters!")
    print("You start with three lives and a weapon to successfully make it through 50 levels of hell.")
    print("There are three doors on each level. Type 'l' to go left, 'r' to go right, and 's' to go straight.")
    print("Behind each door, there lies either a safe haven, a healing station, a shop, or a vicious enemy.")
    print("Safe Haven: Move to the next level / Healing Fountain: Gain a life / Shop: Spend your coins")
    print("When fighting a monster, you will have three options: Shoot ('s'), dodge ('d') or reload ('r').")
    print("Your weapon will start each battle with 1 ammo, so be wise with your choices!")
    
    start = str(input("Good luck and may you venture safely! Type 'r' when you're ready: "))
    if start == 'r':
        p1.game()
    else:
        print("Please type 'r'!")
        exit()

elif start == 'r':
    p1.game()

else:
    print("Please type 'r' or 'y'!")
    exit()