from unittest import TestCase, main

from project.player.advanced import Advanced


class TestAdvanced(TestCase):

    def setUp(self):
        self.user = Advanced("Test")

    def test_init(self):
        self.assertEqual("Test", self.user.username)
        self.assertEqual(250, self.user.health)

    def test_empty_string_raises(self):
        with self.assertRaises(ValueError) as ex:
            user = Advanced("")
        self.assertEqual("Player's username cannot be an empty string.", str(ex.exception))

    def test_negative_health_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.user.health = -20
        self.assertEqual("Player's health bonus cannot be less than zero ", str(ex.exception))

    def test_take_damage(self):
        self.user.take_damage(1)
        self.assertEqual(249, self.user.health)

    def test_life(self):
        self.assertFalse(self.user.is_dead)
        self.user.take_damage(250)
        self.assertEqual(0, self.user.health)
        self.assertTrue(self.user.is_dead)

    def test_take_negative_damage_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.user.take_damage(-1)
        self.assertEqual("Damage points cannot be less than zero.", str(ex.exception))

if __name__ == '__main__':
    main()