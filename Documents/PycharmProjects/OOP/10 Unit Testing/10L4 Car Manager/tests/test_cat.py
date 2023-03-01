from project.car import Car

from unittest import TestCase, main

class CarTests(TestCase):

    def setUp(self):
        self.car = Car("TestMake", "TestModel", 5, 20)

    def test_init(self):
        self.assertEqual("TestMake", self.car.make)
        self.assertEqual("TestModel", self.car.model)
        self.assertEqual(5, self.car.fuel_consumption)
        self.assertEqual(20, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_empty_make_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_with_new_value(self):
        self.car.make = "TestovMake"
        self.assertEqual("TestovMake", self.car.make)

    def test_empty_model_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model_with_new_value(self):
        self.car.model = "TestovModel"
        self.assertEqual("TestovModel", self.car.model)

    def test_negative_fuel_consumption_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -5
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_new_value(self):
        self.car.fuel_consumption = 3
        self.assertEqual(3, self.car.fuel_consumption)

    def test_negative_fuel_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -20
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_new_value(self):
        self.car.fuel_capacity = 25
        self.assertEqual(25, self.car.fuel_capacity)

    def test_negative_fuel_amount_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -20
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_amount_new_value(self):
        self.car.fuel_amount = 25
        self.assertEqual(25, self.car.fuel_amount)

    def test_refuel_negative_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-20)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_fuel_more_than_capacity(self):
        self.car.refuel(25)
        self.assertEqual(20, self.car.fuel_amount)

    def test_refuel_less_than_mix_capacity(self):
        self.car.refuel(18)
        self.assertEqual(18, self.car.fuel_amount)

    def test_drive_with_zero_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(5)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_init_fuel(self):
        car = Car("Car1", "CarModel", 5, 20)
        car.fuel_amount = 30
        car.drive(20)
        self.assertEqual(29, car.fuel_amount)

    def test_refuel_and_drive(self):
        self.car.refuel(5)
        self.car.drive(20)
        self.assertEqual(4, self.car.fuel_amount)


if __name__ == "__main__":
    main()

