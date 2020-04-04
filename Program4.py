#WAP to enter length and breadth of a rectangle and find its perimeter
length, breadth = map(float,input("Enter length and breadth with spaces").split())

def perimeter_of_rectangle(a,b):
    return 2*(a+b)
perimeter = perimeter_of_rectangle(length,breadth)
print("Perimeter of rectangle is", perimeter)