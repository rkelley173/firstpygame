import time
import random
from random import randint
import os

# defines moves the enemy can choose from
MOVESET = ["attack", "defend", "prolonged attack"]

# defines a lot of variables, including name, attack, starting health/attack pots etc.
class Player:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        self.healthpots = 1
        self.attackpots = 1
        self.move = ""

    # ensures health and attack pot vars are met, then modifies variables based on certain conditions
    def consumeHealthPot(self):
        if self.healthpots >= 1:
            if player.health <= 50:
                self.healthpots -= 1
                self.health += 50
                print("Drank a health pot! You now have " + str(self.health) + " health and " + str(self.healthpots) + " healthpots left.")
            elif player.health > 50:
                if player.health == 100:
                    print("You're at full health and can't use a health pot!")
                else:
                    self.healthpots -= 1
                    self.health = 100
                    print("Drank a health pot! You now have " + str(self.health) + " health and " + str(self.healthpots) + " healthpots left.")
        else:
            print("You don't have any health pots to consume!")

    def consumeAttackPot(self):
        if self.attackpots >= 1:
            self.attackpots -= 1
            self.attack += 20
            print("Drank an attack pot! You now have " + str(self.attack) + " attack and " + str(self.attackpots) + " attackpots left.")     
        else:
            print("You don't have any attack pots to consume!")

    # gathers player input for their move, to be called later
    def getPlayerMove(self):
        self.move = input("What do you want to do? ").lower()


    def enemyResponseToPlayer(self):
        # enemyMove = random.sample(MOVESET, 1) - decided to keep in to remind from further error. random
        # sample pulls away two array values and leaves only one in the array and returns that array,
        # meaning a string wasn't registered, but rather an array string. In order to get the input I wanted,
        # I changed it to the below thanks to my friend and the code started working successfully.

        # chooses a random attack for the enemy indexed by the array "MOVESET" at the top
        enemyMove = MOVESET[randint(0, 2)]

        # if both players pick the same move
        if enemyMove == self.move:
            print("You both picked " + self.move + ", so nothing happens!")
        
        # if the player attacks and the enemy defends    
        elif self.move == "attack" and enemyMove == "defend":
            self.health -= self.attack/2
            print("You attack while the " + enemies[0].name + " defends!")
            time.sleep(2)
            print("The " + enemies[0].name + " reflects your attack and deals " + str(self.attack/2) + " damage!")

        # if the player attacks and the enemy prolongs theirs    
        elif self.move == "attack" and enemyMove == "prolonged attack":
            enemies[0].health -= self.attack
            print("You attack while the " + enemies[0].name + " prolongs their attack!")
            time.sleep(2)
            print("The " + enemies[0].name + " took too long to attack you and takes " + str(self.attack) + " damage!" )

        # if the player defends and the enemy attacks    
        elif self.move == "defend" and enemyMove == "attack":
            enemies[0].health -= enemies[0].attack/2
            print("You defend while the " + enemies[0].name + " attacks!")
            time.sleep(2)
            print("You reflect the " + enemies[0].name + "'s attack and deal " + str(enemies[0].attack/2) + " damage!")

        # if the player defends and the enemy prolongs their attack
        elif self.move == "defend" and enemyMove == "prolonged attack":
            self.health -= enemies[0].attack*2
            print("You defend while the " + enemies[0].name + " prolongs their attack!")
            time.sleep(2)
            print("You are left extremely vulnerable to the " + enemies[0].name + " attack and take " + str(enemies[0].attack*2) + " damage!")

        # if the player prolongs their attack and the enemy attacks
        elif self.move == "prolonged attack" and enemyMove == "attack":
            self.health -= enemies[0].attack
            print("You prolong your attack while the " + enemies[0].name + " attacks!")
            time.sleep(2)
            print("You take too long to attack the " + enemies[0].name + "'s attack and take " + str(enemies[0].attack) + " damage!" )

        # if the player prolongs their attacks and the enemy defends
        elif self.move == "prolonged attack" and enemyMove == "defend":
            enemies[0].health -= self.attack*2
            print("You prolong your attack while the " + enemies[0].name + " defends!")
            time.sleep(2)
            print("The " + enemies[0].name + " is left extremely vulnerable to your attack and takes " + str(self.attack*2) + " damage!")
        
        # checks for the help command
        elif self.move == "help":
            print("Game is RPS style. Attack beats Prolonged Attack, Defend beats Attack, and Prolonged Attacks beats defend.")
            time.sleep(3)
            print("By consuming a health pot you regain 50 health, but can't go over 100. By consuming an attack pot, you gain 20 permanent attack.")
            time.sleep(3)
            print("Command list: 'attack', 'defend', 'prolonged attack', 'use healthpot', 'use attackpot'.")

        # if the player wants to use an attack pot
        elif self.move == "use attackpot":
            player.consumeAttackPot()

        # if the player wants to use a health pot
        elif self.move == "use healthpot":
            player.consumeHealthPot()

        # THE FOLLOWING TWO COMMANDS ARE FOR DEBUGGING ONLY AND HAS SUCH WILL BE COMMENTED OUT.
        # FOR FURTHER DEBUGGING UNCOMMENT THESE LINES IN ORDER TO SPEED THROUGH GAME.
        
        # elif self.move == "kill":
        #     enemies[0].health = 0
        #     print("ENEMY KILLED")

        
        # elif self.move == "suicide":
        #     player.health = 0
        #     print("SUICIDED")

        # command cathcer to ensure only valid inputs are made
        else:
            print("That's not a valid input! Try again!")
        time.sleep(2)

    def dropRandomPot(self):
        # pot drop has to be called before enemy is removed from 0 in array
        potDropCheck = random.randint(0,100)
        if potDropCheck <= 35:
            self.healthpots += 1
            print("You found a health pot!")
        elif potDropCheck >= 80:
            self.attackpots += 1
            print("You found an attack pot!")
        else:
            print("You weren't able to loot anything from the " + enemies[0].name + ".")
        print("You now have " + str(self.healthpots) + " health pots and " + str(self.attackpots) + " attack pots.")

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

# stats of the enemy types, refers back to Enemy class formed earlier
enemyLoser = Enemy("Loser", 50, 10)
enemyNotBig = Enemy("Not as Big of a Loser", 75, 15)
enemySemiPop = Enemy("Semi-Popular Guy", 100, 20)
enemyVeryPop = Enemy("Very Popular Guy", 125, 25)
enemyJock = Enemy("School Jock", 150, 30)
enemyChad = Enemy("Chad Himself", 200, 50)

# creates an array of enemies for notational purposes later in the code
enemies = [enemyLoser, enemyNotBig, enemySemiPop, enemyVeryPop, enemyJock, enemyChad]
player = Player(input("What is your name, schoolgoer? "), 100, 20)
print("Welcome, " + player.name + ", to the School of Defined Masculinity!")
time.sleep(2)
print("Everyone in here desires to be a Chad. However, only a select, gifted few can succeed.")
time.sleep(3)
print("You must rise to the challge and claim the title of Ultimate Chad by defeating the beta males.")
time.sleep(2)

# asks the player if they are ready to start, and ensures that they cannot escape until they answer either y or n.
while True:
    continueCheck = input("Are you ready to take on the school? Y/N?").lower()
# if they decide to be cheeky and say no, they receive their wish.
    if continueCheck == "n":
        print("Well, screw you too.")
        time.sleep(2)
        os._exit(1)
# if they dont explicitly say "no" then the game contiues. will be changed later to catch a "stop" command eventually.
    elif continueCheck == "y":
        print("Ok, let's begin then!")
        time.sleep(1)
        print("This game functions like rock, paper, scissors. Instead, the options are Attack, Defend, and Prolonged Attack.")
        time.sleep(3)
        print("Attack beats Prolonged Attack, Defend beats Attack, and Prolonged Attack beats defend.")
        time.sleep(3)
        print("The " + enemies[0].name + " starts off the enemies list!")
        time.sleep(2)
        print("Your move options are to either Attack, Defend, or do a Prolonged Attack.")
        time.sleep(2)
        print("You can also use an attack or health pot by typing 'use healthpot and 'use attackpot'.")
        time.sleep(2)
        print("Type 'help' to see a list of what each command does.")
        time.sleep(2)
        break
    else:
        print("Please enter either 'y' or 'n' to make your choice.")
        time.sleep(2)
        continue


# as long as the player is alive, the code runs. so magical.
while player.health > 0:
    time.sleep(1)
    print("You have " + str(player.health) + " health and " + str(player.attack) + " attack.") 
    time.sleep(1)
    print("The " + enemies[0].name + " has " + str(enemies[0].health) + " health and " + str(enemies[0].attack) + " attack.")
    time.sleep(1)
    # calls the functions defined earlier in the player class
    player.getPlayerMove()
    player.enemyResponseToPlayer()
    if enemies[0].health <= 0:
        print("You take down the " + enemies[0].name + "!")
        time.sleep(2)
        if len(enemies) > 0:
            player.dropRandomPot()
            enemies.remove(enemies[0])
            print("You now face the " + enemies[0].name + "!")
        elif len(enemies) == 0:
            print("Congratulations, " + player.name + "! You have beaten the Chad Himself and now possess total control of the")
            time.sleep(.25)
            print("SCHOOL")
            time.sleep(.25)
            print("OF")
            time.sleep(.25)
            print("DEFINED")
            time.sleep(.25)
            print("MASCULINITY!")
            time.sleep(2)
            print("Thanks for playing!")
            os._exit(1)

# if the player sucks and dies, the program ends :(
print("You fall victim to the " + enemies[0].name + " and lose control of the School of Defined Masculinity!")
time.sleep(3)
# tells the player how many enemies they have defeated before exiting.
enemiesDefeated = 6 - len(enemies)
print("You defeated " + str(enemiesDefeated) + " enemies before falling to the " + enemies[0].name + ".")
print("Thanks for playing!")
os._exit(1)
