#WAP to enter marks of five subjects and calculate total, average & percentage

mark1, mark2, mark3, mark4, mark5 = map(float, input("Enter 5 subject marks: ").split())

def perform_analysis(m1, m2, m3, m4, m5):
  total = m1+m2+m3+m4+m5
  avg = total/5
  percentage = (total/500)*100
  return {"total": total, "avg": avg, "percentage": percentage}

result = perform_analysis(mark1, mark2, mark3, mark4, mark5)
print("Total is ", result["total"], " avearage is ", result["avg"], " percentage is ", result["percentage"])
