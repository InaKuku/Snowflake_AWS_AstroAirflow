from project.software.software import Software


class Hardware:
    def __init__(self, name:str, type:str, capacity:int, memory:int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software:Software):
        if self.memory - self.memory_used >= software.memory_consumption and self.capacity - self.available_capacity >= software.capacity_consumption:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software:Software):
        if software in self.software_components:
            self.software_components.remove(software)

    @property
    def memory_used(self):
        memory_taken = 0
        for softw in self.software_components:
            memory_taken += softw.memory_consumption
        return memory_taken

    @property
    def available_capacity(self):
        capacity_used = 0
        for softw in self.software_components:
            capacity_used += softw.capacity_consumption
        return capacity_used