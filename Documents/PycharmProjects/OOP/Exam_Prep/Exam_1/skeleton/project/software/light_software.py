from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, "Light", int(capacity_consumption+(capacity_consumption*0.5)), int(memory_consumption-(memory_consumption*0.5)))