#codewars kata => https://www.codewars.com/kata/52f3149496de55aded000410/python
from functools import reduce

def sum_digits(number):

  #older solution
  '''results = 0
  for num in str(abs(number)):
    results += int(num)
  return results'''

  #refactored solution
  return sum(int(x) for x in str(abs(number)))

#tests

#should print 1
print(sum_digits(10))
#should print 18
print(sum_digits(99))
#should print 5
print(sum_digits(-32))