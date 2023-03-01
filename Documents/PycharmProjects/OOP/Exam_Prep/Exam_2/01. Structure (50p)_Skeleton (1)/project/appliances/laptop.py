from project.appliances.appliance import Appliance

class Laptop(Appliance):
    def __init__(self):
        super().__init__(cost=1)

# lapt = Laptop()
# for base in lapt.__class__.__bases__:
#     print (base.__name__)