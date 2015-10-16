from abc import ABCMeta, abstractmethod

'''
All characters, playable and unplayable are based off this class
'''
class BaseCharacter(metaclass = ABCMeta):

    @abstractmethod
    def __init__(self, name):
        self.name = name
        self.health = 100

