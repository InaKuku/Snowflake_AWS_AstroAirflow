from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, budget=salary_one + salary_two, members_count=2)
        self.room_cost = 20
        self.appliances = 2 * [TV(), Fridge(), Laptop()]
        self.calculate_expenses(self.appliances)




# room = YoungCouple("FamName", 200, 200)
# # child = Child(20, 3, 4, 5)
# # print(room.calculate_expenses([child], [laptop, fridge]))
# print(room.calculate_appliances_for_the_first)
# print(room.calculate_appliances_for_the_second)