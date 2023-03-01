from project.mammal import Mammal

from unittest import TestCase, main

class MammalTest(TestCase):
    def setUp(self):
        self.mammal = Mammal("Miko", "cat", "meow")

    def test_init(self):
        self.assertEqual("Miko", self.mammal.name)
        self.assertEqual("cat", self.mammal.type)
        self.assertEqual("meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual("Miko makes meow", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual("Miko is of type cat", self.mammal.info())

if __name__ == "__main__":
    main()