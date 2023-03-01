class Mammal:
    def __init__(self, name, mammal_type, sound) -> object:
        self.name = name
        self.type = mammal_type
        self.sound = sound
        self.__kingdom = "animals"

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"

# mammal = Mammal("Miko", "cat", "meow")
# print(mammal.get_kingdom())