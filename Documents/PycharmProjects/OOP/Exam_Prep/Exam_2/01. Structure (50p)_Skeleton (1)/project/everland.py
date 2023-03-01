from project.people.child import Child
from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung
from project.rooms.room import Room
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        if not room in self.rooms:
            self.rooms.append(room)

    def get_monthly_consumptions(self):
        monthly_consumption = 0
        for room in self.rooms:
            monthly_consumption += room.expenses
            if hasattr(room, "room_cost"):
                monthly_consumption += room.room_cost
        return f"Monthly consumption: {monthly_consumption:.2f}$."

    def pay(self):
        result = ""
        for room in self.rooms:
            if hasattr(room, "room_cost"):
                if room.budget >= room.expenses + room.room_cost:
                    room.budget = room.budget - room.expenses - room.room_cost
                    res = f"{room.family_name} paid {(room.expenses + room.room_cost):.2f}$ and have {room.budget:.2f}$ left."
                    result += f"\n{res}"
                    def __repr__(self):
                        return res
                else:
                    res = f"{room.family_name} does not have enough budget and must leave the hotel."
                    self.rooms.remove(room)
                    result += f"\n{res}"
                    def __repr__(self):
                        return res
            else:
                if room.budget >= room.expenses:
                    room.budget = room.budget - room.expenses
                    res = f"{room.family_name} paid {room.expenses:.2f}$ and have {room.budget:.2f}$ left."
                    result += f"\n{res}"
                    def __repr__(self):
                        return res
                else:
                    res = f"{room.family_name} does not have enough budget and must leave the hotel."
                    self.rooms.remove(room)
                    result += f"\n{res}"
                    def __repr__(self):
                        return res
        return result

    def status(self):
        visitors_count = 0
        result = ""
        for room in self.rooms:
            visitors_count += room.members_count
            result += f"\n{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$"
            if hasattr(room, "children"):
                for ind in range(len(room.children)):
                    result += f"\n--- Child {ind + 1} monthly cost: {(room.children[ind].cost * 30):.2f}$"
            if hasattr(room, "appliances"):
                all_appl = 0
                for apl in room.appliances:
                    all_appl += apl.get_monthly_expense()
                result += f"\n--- Appliances monthly cost: {all_appl:.2f}$"
        return f"Total population: {visitors_count}" \
               f"{result}"

# hotel = Everland()
# room1 = AloneOld("Frof", 200)
# hotel.add_room(room1)
# print(hotel.status())
# child_1 = Child(15, 3, 4)
# child_2 = Child(1, 0)
# room_youngcopl_children = YoungCoupleWithChildren("Grag", 3500, 12000, child_1, child_2)
# room_aloneyoung = AloneYoung("Singleton", 1500)
# room_couple = YoungCouple("JustMarried", 2000, 2500)
# hotel.add_room(room_youngcopl_children)
# hotel.add_room(room_aloneyoung)
# hotel.add_room(room_couple)
# print(hotel.pay())
# print(hotel.status())
#
# everland = Everland()
# young_couple = YoungCouple("Johnsons", 150, 205)
#
# child1 = Child(5, 1, 2, 1)
# child2 = Child(3, 2)
# young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)
#
# everland.add_room(young_couple)
# everland.add_room(young_couple_with_children)
#
# print(everland.get_monthly_consumptions())
# print(everland.pay())
# print(everland.status())
