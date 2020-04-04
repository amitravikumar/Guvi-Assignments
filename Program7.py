#WAP to enter temperature in celsius and convert it to farenheit

temp = float(input("Enter temperature in Celsius: "))

def convert_celsius_to_farenheit(t):
  return (t*1.8)+32

farenheit_temp = convert_celsius_to_farenheit(temp)
print("Temperature in Fareheit is ", farenheit_temp)
