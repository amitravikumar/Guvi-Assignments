#WAP to enter P, T & R and calculate simple interest

principal, interest, time = map(float, input().split())

def find_simple_interest(p, t, r):
  print(round((p * t * r) / 100, 2))

find_simple_interest(principal, time, interest)
