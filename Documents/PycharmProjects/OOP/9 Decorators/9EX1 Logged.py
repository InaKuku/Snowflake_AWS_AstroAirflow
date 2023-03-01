def logged(funct):
    def wrapper(*args):
        res = ""
        res += f"you called {funct.__name__}{args}\n"
        res += f"it returned {funct(*args)}"
        return res
    return wrapper

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))