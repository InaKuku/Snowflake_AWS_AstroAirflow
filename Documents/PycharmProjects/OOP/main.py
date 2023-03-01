from timeit import default_timer as timer


def exec_time(func):
    def wrapper(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        end = timer() - start
        return end
    return wrapper

@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result
print(concatenate(["a" for i in range(1000000)]))