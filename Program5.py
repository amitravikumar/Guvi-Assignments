#WAP to enter length and breadth of rectangle and find its area
length, breadth = map(float, input("Enter length & breadth: ").split())

def find_area(a, b):
  return a*b

area = find_area(length, breadth)
print("Area of rectangle is ", area)