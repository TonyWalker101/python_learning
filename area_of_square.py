#codewars kata => https://www.codewars.com/kata/5748838ce2fab90b86001b1a/python

from math import pi

def square_area(A):
  return (2 * A / pi) ** 2

#tests

#should print 1.62
print(square_area(2))
#should print 0
print(square_area(0))
#should print 80
print(square_area(14.05))
#should print 0.41
print(square_area(1))
#should print 4052.85
print(square_area(100))