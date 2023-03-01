from unittest import TestCase, main

from project.vehicle import Vehicle

class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(20, 150)

    def test_init_int(self):
        self.assertEqual(20, self.vehicle.fuel)
        self.assertEqual(20, self.vehicle.capacity)
        self.assertEqual(150, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_init_float(self):
        vehicle = Vehicle(18.5, 155.7)
        self.assertEqual(18.5, vehicle.fuel)
        self.assertEqual(18.5, vehicle.capacity)
        self.assertEqual(155.7, vehicle.horse_power)
        self.assertEqual(1.25, vehicle.fuel_consumption)

    def test_drive_with_enough_fuel(self):
        self.vehicle.drive(15)
        self.assertEqual(1.25, self.vehicle.fuel)

    def test_drive_with_unsufficient_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(35)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_with_more_fuel_than_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(5)
        self.assertEqual(20, self.vehicle.fuel)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_less_than_capacity(self):
        self.vehicle.fuel = 3
        self.vehicle.refuel(5)
        self.assertEqual(8, self.vehicle.fuel)

    def test_drive_and_refuel(self):
        self.vehicle.drive(15)
        self.assertEqual(1.25, self.vehicle.fuel)
        self.vehicle.refuel(15)
        self.assertEqual(16.25, self.vehicle.fuel)

    def test_str(self):
        self.assertEqual("The vehicle has 150 horse power with 20 fuel left and 1.25 fuel consumption", str(self.vehicle))

if __name__ == "__main__":
    main()

