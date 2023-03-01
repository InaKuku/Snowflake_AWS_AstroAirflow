class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}
        self.topping_counter = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    def add_topping(self, topping):
        if self.topping_counter + 1 > self.toppings_capacity:
            raise ValueError("Not enough space for another topping")
        else:
            if not topping.topping_type in self.toppings:
                self.toppings[topping.topping_type] = 0
            self.toppings[topping.topping_type] += topping.weight
            self.topping_counter += 1


    def calculate_total_weight(self):
        toppings_weight = 0
        for top, wgh in self.toppings.items():
            toppings_weight += wgh
        return self.dough.weight + toppings_weight