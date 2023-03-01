from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(TestCase):

    def setUp(self):
        self.hardware = Hardware("Name", "Heavy", 20, 20)

    def test_init(self):
        self.assertEqual("Name", self.hardware.name)
        self.assertEqual("Heavy", self.hardware.type)
        self.assertEqual(20, self.hardware.memory)
        self.assertEqual(20, self.hardware.memory)

    def test_install_software_less_memory_less_capacity(self):
        software = Software("SoftName", "Express", 3, 2)
        self.hardware.install(software)
        self.assertEqual([software], self.hardware.software_components)


    def test_install_software_less_memory_bigger_capacity_raise(self):
        software = Software("SoftName", "Express", 23, 2)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_install_software_bigger_memory_less_capacity_raise(self):
        software = Software("SoftName", "Express", 3, 22)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_uninstall_existing_software(self):
        software = Software("SoftName", "Express", 3, 2)
        self.hardware.install(software)
        self.assertEqual([software], self.hardware.software_components)
        self.hardware.uninstall(software)
        self.assertEqual([], self.hardware.software_components)




if __name__ == '__main__':
    main()