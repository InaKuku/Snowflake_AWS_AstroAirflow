# class Animal:
#     def __init__(self, species):
#         self.species = species
#
#     def get_species(self):
#         return self.species
#
#
# def animal_sound(animals: list):
#     for animal in animals:
#         if animal.species == 'cat':
#             print('meow')
#         elif animal.species == 'dog':
#             print('woof-woof')
#
#
# animals = [Animal('cat'), Animal('dog')]
# animal_sound(animals)

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def animal_sound(self):
        pass

class Dog(Animal):

    def animal_sound(self):
        pass

class Cat(Animal):

    def animal_sound(self):
        pass