from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.hardware.power_hardware import Hardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        for obj in System._hardware:
            if obj.name == name:
                return
        return System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        for obj in System._hardware:
            if obj.name == name:
                return
        return System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int,
                                  memory_consumption: int) -> object:
        try:
            hardw = [hardw for hardw in System._hardware if hardw.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardw.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardw = [hardw for hardw in System._hardware if hardw.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardw.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardw = [hardw for hardw in System._hardware if hardw.name == hardware_name][0]
            softw = [softw for softw in System._software if softw.name == software_name][0]
            hardw.uninstall(softw)
            System._software.remove(softw)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        all_memory = 0
        total_capacity = 0
        sys_memory_taken = 0
        total_used_space = 0
        for hardw in System._hardware:
            all_memory += hardw.memory
            total_capacity += hardw.capacity
            sys_memory_taken += hardw.memory_used
            total_used_space += hardw.available_capacity

        return "System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {sys_memory_taken} / {all_memory}\n" \
               f"Total Capacity Taken: {total_used_space} / {total_capacity}"

    @staticmethod
    def system_split():
        result = ""
        comp_list = "None"
        for hardw in System._hardware:
            express_counter = 0
            light_counter = 0
            for softw in hardw.software_components:
                if softw.type == "Express":
                    express_counter += 1
                elif softw.type == "Light":
                    light_counter += 1
            if len(hardw.software_components) > 0:
                comp_list = ', '.join([soft.name for soft in hardw.software_components])
            result += f"Hardware Component - {hardw.name}"
            result += f"\nExpress Software Components: {express_counter}"
            result += f"\nLight Software Components: {light_counter}"
            result += f"\nMemory Usage: {hardw.memory_used} / {hardw.memory}"
            result += f"\nCapacity Usage: {hardw.available_capacity} / {hardw.capacity}"
            result += f"\nType: {hardw.type}"
            result += f"\nSoftware Components: {comp_list}"
        return result





# system = System()
# system.register_heavy_hardware("Name", 29, 30)
# system.register_power_hardware("Some_Name", 29, 30)
# print(system.register_express_software("Some_Name", "Some_Software", 3, 3))
# print(system.register_express_software("Non_Existing_Name", "Some_Software", 31, 26))
# print(system.register_express_software("Some_Name", "Some_Software_23", 1, 5))
# print(system.release_software_component("O_Name", "Some_Software_23"))
# print(system.analyze())
# print(system.system_split())
