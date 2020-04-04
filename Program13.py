#WAP to enter the base and height of a triangle and find its area

base, height = map(float, input("Enter base & height: ").split())

def find_area(b, h):
  return (b*h)/2

result = find_area(base, height)
print("Area of triangle is ", result)