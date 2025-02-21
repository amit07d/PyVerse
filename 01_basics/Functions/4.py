# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def circle(radius):
    area = int(2 ** radius * math.pi)
    circumference = int(2 * radius * math.pi)
    
    return area, circumference

a,c = circle(3)

print(a,"\n",c)