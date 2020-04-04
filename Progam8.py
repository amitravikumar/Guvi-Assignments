#WAP to enter temperature in farenheit and convert it to celsius

temp = float(input("Enter temperature in Farenheit: "))

def convert_farenheit_to_celsius(t):
  return ((t-32)*(5/9))

celsius_temp = convert_farenheit_to_celsius(temp)
print("Temperature in Celsius is ", celsius_temp)