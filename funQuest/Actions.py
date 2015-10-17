from abc import ABCMeta, abstractmethod

'''
This module will handle all of the actions for the
player as well as for the NPC's and the enemies.
If this gets too big I will divide it up into
seperate modules
'''

#should I make a method for attack or a class for
#actions?

class Actions(metaclass = ABCMeta):

    @abstractmethod
    def attack(self, target):
        pass
    #pass works for abstract functions

    @abstractmethod
    def talk(self, target = ""):
        pass

    @abstractmethod
    def use(self, item, target):
        pass

    @abstractmethod
    def pickUp(self, item):
        pass
