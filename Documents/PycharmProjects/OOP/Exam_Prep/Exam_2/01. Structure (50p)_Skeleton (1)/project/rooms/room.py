from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.people.child import Child

#family name or name
# expenses - lists of children or lists of appliances


class Room:
    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    def calculate_expenses(self, *args):
        total_expenses = 0
        for list_index in range(len(args)):
            for element in args[list_index]:
                if element.__class__.__name__ == "Child":
                    total_expenses += 30 * element.cost
                else:
                    for base in element.__class__.__bases__:
                        if base.__name__ == "Appliance":
                            total_expenses += element.get_monthly_expense()
        self.expenses = total_expenses

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

#
# room = Room("One", 200, 3)
# laptop = Laptop()
# fridge = Fridge()
# child = Child(20, 3, 4, 5)
# print(room.calculate_expenses([child], [laptop, fridge]))
# print(room.expenses)

# room = Room("Johnson", 1600, 2)
# child = Child(-3, -2, 1)
# print(room.calculate_expenses([child]))
# room.children = [child]
# print(room.children)


