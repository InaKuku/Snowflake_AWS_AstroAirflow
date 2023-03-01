from functools import reduce

class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x*y, args)

    # @staticmethod
    # def multiply(*args):
    #     mult = 1
    #     for arg in args:
    #         mult *= arg
    #     return mult

    @staticmethod
    def divide(*args):
        return reduce(lambda x, y: x/y, args)

    # @staticmethod
    # def divide(*args):
    #     dvs = args[0]
    #     for dv_index in range(1, len(args)):
    #         dvs = dvs / args[dv_index]
    #     return dvs

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x-y, args)

    # @staticmethod
    # def subtract(*args):
    #     dvs = args[0]
    #     for dv_index in range(1, len(args)):
    #         dvs = dvs - args[dv_index]
    #     return dvs


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))