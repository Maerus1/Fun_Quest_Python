import Base
import Weapon

'''
This program simply allows the user to create Player objects and give him a
weapon object. You can check the player's stats as well
'''

class Player(Base.BaseCharacter):
    def __init__(self, name, weaponName):
        super(Player, self).__init__(name)
        self.weapon = Weapon.Weapon(weaponName)

    def printStats(self):
        print(self.name)
        print(self.health)
        print(self.weapon.name)

    def attack(self, target):
        target.health -= self.weapon.damage
        #This is the beginning of my combat system

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
