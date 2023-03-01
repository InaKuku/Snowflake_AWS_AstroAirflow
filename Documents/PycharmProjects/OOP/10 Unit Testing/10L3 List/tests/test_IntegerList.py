from project.IntegerList import IntegerList

from unittest import TestCase, main

class IntegerListTests(TestCase):

    def setUp(self):
        self.integerlist = IntegerList(1, 2, 5.6)


    def test_does_init_create_all_attributes(self):
        self.assertEqual([1, 2], self.integerlist._IntegerList__data)


    def test_if_adding_float_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.integerlist.add(5.6)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_if_adding_int_works(self):
        self.integerlist.add(6)
        self.assertEqual([1, 2, 6], self.integerlist.get_data())

    def test_if_removing_index_out_of_range_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.integerlist.remove_index(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_if_removing_in_range_index_works(self):
        self.assertEqual(1, self.integerlist.remove_index(0))
        self.assertEqual([2], self.integerlist.get_data())

    def test_if_get_gives_right_num_index_in_range(self):
        self.assertEqual(1, self.integerlist.get(0))

    def test_if_get_with_index_out_of_range_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.integerlist.get(8)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_right_index_with_right_num(self):
        self.integerlist.insert(1, 3)
        self.assertEqual([1, 3, 2], self.integerlist.get_data())

    def test_insert_out_of_range_index_with_right_num(self):
        with self.assertRaises(IndexError) as ex:
            self.integerlist.insert(2, 3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_in_range_index_with_wrong_num(self):
        with self.assertRaises(ValueError) as ex:
            self.integerlist.insert(1, 3.1)
        self.assertEqual("Element is not Integer", str(ex.exception))


    def test_get_biggest(self):
        self.assertEqual(2, self.integerlist.get_biggest())

    def test_get_biggest_after_adding(self):
        self.integerlist.add(100)
        self.assertEqual(100, self.integerlist.get_biggest())

    def test_get_index(self):
        self.assertEqual(1, self.integerlist.get_index(2))


if __name__ == "__main__":
    main()



