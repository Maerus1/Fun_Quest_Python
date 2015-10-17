import Base
import Weapon
import Actions

'''
This program simply allows the user to create Player objects and give him a
weapon object. You can check the player's stats as well
'''

class Player(Base.BaseCharacter, Actions.Actions):
    def __init__(self, name, weaponName):
        super(Player, self).__init__(name)
        self.weapon = Weapon.Weapon(weaponName)

    def printStats(self):
        print(self.name)
        print(self.health)
        print(self.weapon.name)
        
    def attack(self, target):
        target.health -= self.weapon.damage
        print ("You attack the enemy!")
        print ("You do " + str(self.weapon.damage) + " damage!")
        
        self.health -= target.damage
        print ("The enemy attacks you!")
        print ("You take " + str(target.damage) + " damage!")

        print("The enemy has: " + str(target.health) + " health.")
        print("You have: " + str(self.health) + " health.")

    def talk(self, target = ""):
        print("Hello " + str(target) + "!")

    def use(self, item, target):
        #I'll need to add if statements in here to limit the choice of items
        print("You used: " + str(item) + " on " + str(target) + "!")

    def pickUp(self, item):
        #I'll need to have the thing picked up added to the inventory
        print("You picked up: " + str(item) + "!")

    #if you do not override at least one(or all?
    #I'm not sure), then the inheriting class also
    #becomes abstract
        


'''
This is a class that will hold the attributes and behaviours of the enemies
for the game. They will be instantiated in main for now, but I may have a file
to instantiate my objects apart from main in the future
'''

class Enemy(Base.BaseCharacter):
    def __init__(self, name):
        super(Enemy, self).__init__(name)
        self.damage = 8
        self.health = 30
