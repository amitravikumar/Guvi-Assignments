#WAP to enter P, T & R and calculate compound interest

principal, interest, time = map(float, input().split())

def find_compound_interest(p, t, r):
  print(p*(pow((1+r/100),t)))

find_compound_interest(principal, time, interest)