#codewars kata => https://www.codewars.com/kata/563f037412e5ada593000114/python

def calculate_years(principal, interest, tax, desired):
  year = 0
  sum = principal

  while True:
    if sum >= desired:
      return year
    else:
      year += 1
      sum += sum * interest
      sum -= ((sum * interest)*tax)
  
#tests

#should print 3
print(calculate_years(1000, 0.05, 0.18, 1100))
#should print 14
print(calculate_years(1000,0.01625,0.18,1200))
#should print 0
print(calculate_years(1000,0.05,0.18,1000))