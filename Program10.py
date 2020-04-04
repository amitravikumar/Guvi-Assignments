#WAP to find the power of any number

number, power = map(int, input("Enter number and power: ").split())

def find_power(n,p):
  return n**p

result = find_power(number, power)
print(number, "rasied to the power ", power, " is ", result)