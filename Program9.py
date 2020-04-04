#WAP to convert days into years, weeks & days

number_of_days = int(input("Enter number of days: "))

def find_years_weeks_days(days):
  year = int(days / 365) 
  week = int((days % 365) / 7) 
  days = (days % 365) % 7 
      
  print("years = ",year,"\nweeks = ",week,"\ndays = ",days)

find_years_weeks_days(number_of_days)