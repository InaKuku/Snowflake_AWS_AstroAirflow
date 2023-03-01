from project.worker import Worker

from unittest import TestCase, main

class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker("Bro", 5000, 100)

    def test_is_worker_initialized_with_correct_name_salary_energy(self):
        self.assertEqual("Bro", self.worker.name)
        self.assertEqual(5000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_if_energy_is_incremented_after_the_rest_method(self):
        self.assertEqual(100, self.worker.energy)
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_if_worker_works_with_negative_energy_raises(self):
        worker = Worker("Test", 1, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_if_workers_money_is_increased_after_work_method(self):
        self.assertEqual(0, self.worker.money)
        self.worker.work()
        self.assertEqual(5000, self.worker.money)

    def test_workers_energy_is_decreased_after_work(self):
        self.assertEqual(100, self.worker.energy)
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_get_info_proper_string(self):
        actual_result = self.worker.get_info()
        expected_result = "Bro has saved 0 money."
        self.assertEqual(expected_result, actual_result)




if __name__ == "__main__":
    main()



