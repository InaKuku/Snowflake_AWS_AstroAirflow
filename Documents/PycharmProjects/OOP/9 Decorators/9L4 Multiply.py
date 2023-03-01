def multiply(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            res = 0
            for _ in range(times):
                res += function(*args, **kwargs)
            return res
        return wrapper
    return decorator

@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))