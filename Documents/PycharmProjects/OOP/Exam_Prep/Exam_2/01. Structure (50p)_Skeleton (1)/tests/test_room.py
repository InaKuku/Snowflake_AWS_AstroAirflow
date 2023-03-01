from unittest import TestCase, main

from project.people.child import Child
from project.rooms.room import Room


class TestRoom(TestCase):
    def setUp(self):
        self.room = Room("Johnson", 1600, 2)
        # child = Child(3, 2, 1)
        # self.room.children = [child]

    def test_init(self):
        self.assertEqual("Johnson", self.room.family_name)
        self.assertEqual(1600, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual([], self.room.children)
        # self.assertEqual(1, len(self.room.children))
        self.assertEqual(0, self.room.expenses)

    def test_calculate_expenses(self):
        self.room.expenses = 150
        self.assertEqual(150, self.room.expenses)

    def test_calculate__negative_expenses(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -150
        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_calculate_expenses_with_child_and_appliances(self):
        child = Child(3, 2, 1)
        self.room.calculate_expenses([child])
        self.assertEqual(180, self.room.expenses)

    def test_calculate_expenses_with_no_args(self):
        self.room.calculate_expenses()
        self.assertEqual(0, self.room.expenses)

    def test_calculate_negative_expense_raise(self):
        child = Child(-3, -2, 1)
        with self.assertRaises(ValueError) as ex:
            self.room.calculate_expenses([child])
        self.assertEqual("Expenses cannot be negative", str(ex.exception))

if __name__ == '__main__':
    main()




