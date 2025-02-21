# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):
    return(sum(args))

print("sum of all num -",sum_all(1,7,5,8,6,7,2,6))
print("sum of all num =",sum_all(1,88,44,112,5,7,5))

