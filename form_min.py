#codewars kata => https://www.codewars.com/kata/5ac6932b2f317b96980000ca/python

from collections import Counter

def min_value(digits):
  unique_digits = sorted(list(Counter(digits)))
  string_unique_digits = map(lambda x: str(x), unique_digits)
  return int("".join(string_unique_digits))

#tests

#should print 13
print(min_value([1, 3, 1]))
#should print 457
print(min_value([4, 7, 5, 7]))
#should print 148
print(min_value([4, 8, 1, 4]))