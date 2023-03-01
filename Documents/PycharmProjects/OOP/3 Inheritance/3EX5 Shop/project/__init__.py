from project.product import Product
from project.drink import Drink
from project.food import Food
from project.product_repository import ProductRepository

pr_1 = Food("butter")
pr_2 = Drink("tea")
pr = ProductRepository()
pr.add(pr_1)
pr_1.decrease(6)
pr_1.decrease(3)
pr.add(pr_2)
pr_2.increase(3)
print(pr.find("butter"))
pr.remove("tea")
pr_3 = Food("Meat")
pr.add(pr_3)
print(repr(pr))