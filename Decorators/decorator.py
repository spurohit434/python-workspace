import time
import functools

def cache(func):
    cache_value = {}
    print("cache value is:" , cache_value)
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache_value:
            print("flow here")
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_func(a,b):
    time.sleep(4)
    return a+b

@cache
def info(x,y):
    time.sleep(2)
    return x*y


print(info.__name__)

# curr_time = time.time()
# print(curr_time)
# print(long_running_func(4,3))
# curr_time_taken = time.time()
# print(curr_time_taken)
# print("time taken by func: ", curr_time_taken - curr_time )
# print(long_running_func(4,3))