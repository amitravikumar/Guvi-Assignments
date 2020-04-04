#WAP to find the area of an equilateral triangle

import math

side = float(input("Enter the side: "))

def find_area_of_triangle(a):
  return(round(((1/4) * math.sqrt(3) * (a**2)), 2))

result = find_area_of_triangle(side)
print("Area of equilateral triangle is ", result)