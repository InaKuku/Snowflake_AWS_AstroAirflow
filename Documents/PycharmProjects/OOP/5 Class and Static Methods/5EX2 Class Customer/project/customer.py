class Customer:
    def __init__(self, name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__ (self):
        result = ""
        result += f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ("
        for dv in self.rented_dvds:
            if not self.rented_dvds.index(dv) == len(self.rented_dvds)-1:
                result += f"{dv.name}, "
            else:
                result += f"{dv.name}"
        result += ")"
        return result
