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
