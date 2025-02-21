# username = "codewithme"

# def func():
#     username = "code"
#     print(username)
    
# print(username)
# func()

# x = 88

# def func2(y):
#     z = x + y
#     return z 

# result = func2(1)
# print(result)



def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(4))  # Output: 16
print(g(4))  # Output: 64
