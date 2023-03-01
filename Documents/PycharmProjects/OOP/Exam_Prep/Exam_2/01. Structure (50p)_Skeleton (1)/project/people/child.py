class Child:
    
    cost: float 
    def __init__(self, food_cost: int, *toys_cost):
        self.food_cost = food_cost
        self.toys_cost = sum(toys_cost)
        self.cost = self.food_cost + self.toys_cost


# child = Child(20, 3, 4, 5)
# print(child.cost)
# print(child.__class__.__name__)