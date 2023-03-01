def even_parameters(func):
    def wrapper(*args):
        for arg in args:
            if not type(arg) == int:
                return "Please use only even numbers!"
            if not arg % 2 == 0:
                return "Please use only even numbers!"
        return func(*args)
    return wrapper



@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))