# Problem 1: Timing Function Execution
# Problem: Write a decorator that measures the time a function takes to execute.


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} seconds")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)
    
    return f"function executes in {n} seconds"
print(example_function(2))





















# import time


# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} ran in {end - start} time")
#         return result
#     return wrapper

# @timer
# def example_function(n):
#     time.sleep(n)
#     return f"function execute {n} seconds"
# print(example_function(2))