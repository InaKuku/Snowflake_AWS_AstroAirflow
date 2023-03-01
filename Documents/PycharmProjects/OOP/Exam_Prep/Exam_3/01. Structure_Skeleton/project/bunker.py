from project.medicine.medicine import Medicine
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.supply import Supply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_list = []
        for a_supply in self.supplies:
            if isinstance(a_supply, FoodSupply):
                food_list.append(a_supply)
        if len(food_list) == 0:
            raise IndexError("There are no food supplies left!")
        return food_list

    @property
    def water(self):
        water_list = []
        for a_supply in self.supplies:
            if isinstance(a_supply, WaterSupply):
                water_list.append(a_supply)
        if len(water_list) == 0:
            raise IndexError("There are no water supplies left!")
        return water_list

    @property
    def painkillers(self):
        painkillers_list = []
        for a_supply in self.medicine:
            if isinstance(a_supply, Painkiller):
                painkillers_list.append(a_supply)
        if len(painkillers_list) == 0:
            raise IndexError("There are no painkillers left!")
        return painkillers_list

    @property
    def salves(self):
        salves_list = []
        for a_supply in self.medicine:
            if isinstance(a_supply, Salve):
                salves_list.append(a_supply)
        if len(salves_list) == 0:
            raise IndexError("There are no salves left!")
        return salves_list

    def add_survivor(self, survivor: Survivor):
        if not survivor in self.survivors:
            self.survivors.append(survivor)
        else:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")


    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            if medicine_type == "Painkiller":
                if len(self.painkillers) > 0:
                    self.medicine.remove(self.painkillers[len(self.painkillers)-1])
                    Painkiller().apply(survivor)
                    return f"{survivor.name} healed successfully with {medicine_type}"
            elif medicine_type == "Salve":
                if len(self.salves) > 0:
                    self.medicine.remove(self.salves[len(self.salves) - 1])
                    Salve().apply(survivor)
                    return f"{survivor.name} healed successfully with {medicine_type}"


    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            if sustenance_type == "FoodSupply":
                if len(self.food) > 0:
                    self.supplies.remove(self.food[len(self.food) - 1])
                    FoodSupply().apply(survivor)
                    return f"{survivor.name} sustained successfully with {sustenance_type}"
            elif sustenance_type == "WaterSupply":
                if len(self.water) > 0:
                    self.supplies.remove(self.water[len(self.water) - 1])
                    WaterSupply().apply(survivor)
                    return f"{survivor.name} sustained successfully with {sustenance_type}"


    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= (survivor.age * 2)
            # survivor.needs_sustenance = True
            self.sustain(survivor, "WaterSupply")
            self.sustain(survivor, "FoodSupply")

bunker = Bunker()
survivor1 = Survivor("S1", 23)
painkiller1 = Painkiller()
bunker.add_medicine(painkiller1)
bunker.heal(survivor1, "Painkiller")
survivor1.health = 90
bunker.heal(survivor1, "Painkiller")
# survivor2 = Survivor("S2", 25)
# survivor3 = Survivor("S3", 25)
bunker.add_survivor(survivor1)
# bunker.add_survivor(survivor2)
# bunker.add_survivor(survivor3)
# painkiller2 = Painkiller()

# bunker.add_medicine(painkiller2)
# salve1 = Salve()
# salve2 = Salve()
# bunker.add_medicine(salve1)
# bunker.add_medicine(salve2)
bread = FoodSupply()
bread1 = FoodSupply()
tomato = FoodSupply()
water = WaterSupply()
water1 = WaterSupply()
water2 = WaterSupply()
bunker.add_supply(bread)
bunker.add_supply(bread1)
bunker.add_supply(tomato)
bunker.add_supply(water)
bunker.add_supply(water1)
bunker.add_supply(water2)
print(bunker.next_day())
print(bunker.next_day())
# print(bunker.sustain(survivor1, "FoodSupply"))
# print(bunker.sustain(survivor1, "WoterSupply"))
# bunker.heal(survivor2, "Painkiller")
# bunker.heal(survivor2, "Painkiller")
# bunker.heal(survivor3, "Painkiller")

