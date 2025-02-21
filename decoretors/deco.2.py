# Problem 2: Debugging Function Calls
# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

import time
import functools

def debug(func):
    @functools.wraps(func)  # Preserve function metadata
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k}={v}" for k, v in kwargs.items())

        # Handling cases where there are no kwargs
        if kwargs_value:
            print(f"calling: {func.__name__} with args ({args_value}) and kwargs ({kwargs_value})")
        else:
            print(f"calling: {func.__name__} with args ({args_value})")

        return func(*args, **kwargs)
    
    return wrapper

@debug
def example_function(n):
    time.sleep(n)
    return f"function executes in {n} seconds"

print(example_function(2))

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

greet("Amit", greeting="Morning")




# def debug(func):
#     def wrapper(*args, **kwargs):
#         print(f"calling function {func.__name__} with args:{args} kwargs:{kwargs}")
#         return func(*args, **kwargs)
#     return wrapper

# @debug
# def example_function(a, b):
#     return a + b
# print(example_function(3,b = 5))