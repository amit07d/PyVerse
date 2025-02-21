#  Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def keyword(**kwargs):
    print(kwargs)
    
keyword(name="Amit", from_="Barasat", college="Brainware")
print(type(keyword)) 
