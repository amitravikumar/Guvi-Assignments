#WAP to enter two numbers and perform all arithmetic operations
num1, num2 = map(int, input("Enter two numbers: ").split())

def perform_arithmetic_operations(a, b):
  print("Addition ", a+b)
  print("Subtraction", a-b)
  print("Multiplication", a*b)
  print("Division ", a/b)
  print("Modulus ", a%b)
  print("Exponentiation", a**b)
  print("Floor division ", a//b)

perform_arithmetic_operations(num1, num2)