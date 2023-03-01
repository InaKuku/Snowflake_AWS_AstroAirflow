from unittest import TestCase, main

from project.player.beginner import Beginner


class TestBeginner(TestCase):

    def test_init(self):
        user = Beginner("Test")
        self.assertEqual("Test", user.username)
        self.assertEqual(50, user.health)

    def test_empty_string_raises(self):
        with self.assertRaises(ValueError) as ex:
            user = Beginner("")
        self.assertEqual("Player's username cannot be an empty string.", str(ex.exception))

    def test_negative_health_raises(self):
        user = Beginner("Test")
        with self.assertRaises(ValueError) as ex:
            user.health = -20
        self.assertEqual("Player's health bonus cannot be less than zero ", str(ex.exception))

    def test_take_damage(self):
        user = Beginner("Test")
        user.take_damage(1)
        self.assertEqual(49, user.health)

    def test_take_negative_damage_raises(self):
        user = Beginner("Test")
        with self.assertRaises(ValueError) as ex:
            user.take_damage(-1)
        self.assertEqual("Damage points cannot be less than zero.", str(ex.exception))



if __name__ == '__main__':
    main()