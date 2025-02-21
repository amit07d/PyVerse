# # # input_str = "wgugededw"

# # # for char in input_str:
# # #     print(char)
# # #     if input_str.count(char) == 1:
# # #         print("char is: ", char)
# # #         break


# # # number = 7
# # # factorial = 1

# # # while number > 0:
# # #     factorial *= number
# # #     number -= 1
# # # print("Factorial:", factorial)

# # # import math
# # # print(math.factorial(7))


# # # while True:
# # #     try:
# # #         number = int(input("Enter number b/w 1 and 10: ")) 
        
# # #         if 1 <= number <= 10:
# # #             print("Thanks")
# # #             break  
# # #         else:
# # #             print("Please try again") 
    
# # #     except ValueError:  
# # #         print("Invalid Input! Please enter a number.")  


# # # number = 47
# # # is_prime = True

# # # if number > 1:
# # #     for i in range(2, number):
# # #         if(number % i) == 0:
# # #             is_prime = False
# # #             break
        
        
# # #     print(is_prime)


        
# # # num = int(input("Enter a number: "))

# # # if num < 2:  
# # #     print(num, "is NOT a Prime Number")
# # # else:
# # #     is_prime = True
# # #     for i in range(2, num):
# # #         if num % i == 0:
# # #             is_prime = False  
# # #             break
    
# # #     if is_prime:
# # #         print(num, "is a Prime Number")
# # #     else:
# # #         print(num, "is NOT a Prime Number")


items = ["apple", "banana", "orange", "apple", "mango"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate: ", item)
        break
    unique_items.add(item)


# # # import time

# # # wait_times = 1
# # # max_retries = 5
# # # attemps = 0

# # # while attemps < max_retries:
# # #     print("Attempts", attemps + 1, "- wait-time", wait_times )
# # #     time.sleep(wait_times)
# # #     wait_times *= 2
# # #     attemps += 1


# # num = int(input("Enter a number: "))

# # if num < 2:
# #     print(num, "This is not a prime number")
    
# # else:
# #     is_prime = True
# #     for i in range(2, num):
# #         if num % i == 0:
# #             is_prime = False
# #             break
        
# # if is_prime:
# #     print(num ,"is a prime number")
    
# # else:
# #     print(num, "is not  a prime number")


# # cal the 7 num fact

# num = int(input("Enter a number: "))

# factorial = 1

# if num < 0:
#     print("Factorial is not defined for negative numbers")

# else: 
#     for i in range(1, num + 1):
#         factorial *= i
# print("factorial of", num, "is", factorial)