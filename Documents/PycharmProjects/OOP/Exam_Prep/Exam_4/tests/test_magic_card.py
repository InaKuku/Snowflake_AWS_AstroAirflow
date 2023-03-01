from unittest import TestCase, main

from project.card.magic_card import MagicCard


class TestMagicCard(TestCase):

    def setUp(self):
        self.card = MagicCard("Test")

    def test_init(self):
        self.assertEqual("Test", self.card.name)
        self.assertEqual(5, self.card.damage_points)
        self.assertEqual(80, self.card.health_points)

    def test_empty_str_raises(self):
        with self.assertRaises(ValueError) as ex:
            card = MagicCard("")
        self.assertEqual("Card's name cannot be an empty string.", str(ex.exception))

    def test_damage_points_less_than_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.card.damage_points = -12
        self.assertEqual("Card's damage points cannot be less than zero.", str(ex.exception))

    def test_health_points_less_than_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.card.health_points = -12
        self.assertEqual("Card's HP cannot be less than zero.", str(ex.exception))

if __name__ == '__main__':
    main()