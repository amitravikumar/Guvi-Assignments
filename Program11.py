#WAP to find the square root of any number
import math

number = int(input("Enter the number: "))

def find_square_root(n):
  return math.sqrt(n)

result = find_square_root(number)
print("Square root of ",number," is ", result)
