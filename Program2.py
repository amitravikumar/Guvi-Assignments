#WAP to enter two numbers and find their sum
num1,num2 = map(int,input("Enter two numbers with spaces :").split())

def sum_of_two_numbers(a,b):
    return a+b
result = sum_of_two_numbers(num1,num2)
print("sum of two numbers is",result)
