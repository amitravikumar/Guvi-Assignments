#WAP to enter radius of a circle and find its diameter, circumference & area
import math

radius = float(input("Enter radius of circle: "))

def diameter_circumference_area(r):
  dia = 2*r
  circum = 2* math.pi*r
  area = math.pi * (r**2)
  return {"diameter": round(dia,2), "circumference": round(circum,2), "area": round(area,2)}

result = diameter_circumference_area(radius)
print("Diameter of circle is " + str(result["diameter"]) + " Circumference is "+ str(result["circumference"]) + " Area is "+str(result["area"]))