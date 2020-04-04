#WAP to enter two angles of a triangle and find the third angle

angle1, angle2 = map(float, input("Enter two angles: ").split())

def find_third_angle(a, b):
  return 180-(a+b)

result = find_third_angle(angle1, angle2)
print("Third angle is ", result)