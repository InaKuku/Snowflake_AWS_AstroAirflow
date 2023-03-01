from unittest import TestCase, main

from project.card.trap_card import TrapCard


class TestTrapCard(TestCase):

    def setUp(self):
        self.card = TrapCard("Test")

    def test_init(self):
        self.assertEqual("Test", self.card.name)
        self.assertEqual(120, self.card.damage_points)
        self.assertEqual(5, self.card.health_points)

    def test_empty_str_raises(self):
        with self.assertRaises(ValueError) as ex:
            card = TrapCard("")
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