# Problem: Write a generator function that yields even numbers up to a specified limit.

# def even_num(limit):
#     li = []
    
#     for i in range(2, limit + 1, 2):
#         li.append(i)
#     return li

# print(even_num(10))


def even_num(limit):
    for i in range(2, limit + 1, 2):
        yield(i)
        
for num in even_num(10):
    print(num)