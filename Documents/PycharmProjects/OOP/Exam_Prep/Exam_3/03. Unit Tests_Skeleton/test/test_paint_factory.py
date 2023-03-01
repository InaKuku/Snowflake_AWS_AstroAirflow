from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPainFactory(TestCase):
    def setUp(self):
        self.painfact = PaintFactory("blue", 20)
        self.ingredients = {}

    def test_init(self):
        self.assertEqual("blue", self.painfact.name)
        self.assertEqual(20, self.painfact.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.painfact.valid_ingredients)

    def test_add_igredient_positive(self):
        self.painfact.add_ingredient("yellow", 3)
        self.assertEqual({"yellow": 3}, self.painfact.ingredients)

    def test_add_igredient_not_valid_ingredient_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.painfact.add_ingredient("grey", 3)
        self.assertEqual("Ingredient of type grey not allowed in PaintFactory", str(ex.exception))

    def test_add_igredient_not_enough_space_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.painfact.add_ingredient("yellow", 23)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_igredient_product_type_not_in_ingredients(self):
        self.painfact.add_ingredient("yellow", 3)
        self.painfact.add_ingredient("blue", 3)
        self.assertEqual({"yellow": 3, "blue": 3}, self.painfact.ingredients)

    def test_add_igredient_product_type_with_existing_ingredient(self):
        self.painfact.add_ingredient("yellow", 3)
        self.painfact.add_ingredient("yellow", 3)
        self.assertEqual({"yellow": 6}, self.painfact.ingredients)

    def test_remove_ingredient_normal(self):
        self.painfact.add_ingredient("yellow", 3)
        self.painfact.remove_ingredient("yellow", 2)
        self.assertEqual({"yellow": 1}, self.painfact.ingredients)

    def test_remove_ingredient_less_than_0_raises(self):
        self.painfact.add_ingredient("yellow", 3)
        with self.assertRaises(ValueError) as ex:
            self.painfact.remove_ingredient("yellow", 5)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_not_existing_ingredient_raises(self):
        self.painfact.add_ingredient("yellow", 3)
        with self.assertRaises(KeyError) as ex:
            self.painfact.remove_ingredient("blue", 5)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

if __name__ == '__main__':
    main()