# 2 Lab
# Classes and Objects

# Create a class called Vet. Upon initialization it should receive a name (string). It should also have an instance attribute called animals (empty list by default). There should also be 2 class attributes: animals (empty list) which will store the total amount of animals for all vets; space (5 by default). You should create 3 instance methods
# ⦁	register_animal(animal_name)
# ⦁	If there is space in the vet clinic add the animals to both animals' lists and return a message: "{name} registered in the clinic"
# ⦁	Otherwise return "Not enough space"
# ⦁	unregister_animal(animal_name)
# ⦁	If the animals is in the clinic, remove it from both animals lists and return "{animals} unregistered successfully"
# ⦁	Otherwise, return "{animals} not in the clinic"
# ⦁	info() – returns: "{vet_name1} has {number_animals} animals. {space_left_in_clinic} space left in clinic"

class Vet:
    animals = []
    space = 5
    def __init__(self, name: str):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        if Vet.space > 0:
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)
            Vet.space -= 1
            return f"{animal_name} registered in the clinic"
        else:
            return "Not enough space"

    def unregister_animal(self, animal_name):
        if animal_name in Vet.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            Vet.space += 1
            return f"{animal_name} unregistered successfully"
        else:
            return f"{animal_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"



peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())


