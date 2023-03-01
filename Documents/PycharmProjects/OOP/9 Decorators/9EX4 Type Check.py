def type_check(type_for_check):
    def decorator(func):
        def wrapper(for_check):
            if type(for_check) == type_for_check:
                return func(for_check)
            return "Bad Type"
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
