#codewars kata => https://www.codewars.com/kata/57f780909f7e8e3183000078/python

from functools import reduce

def grow(arr):
  return reduce(lambda x,y: x*y, arr)

#tests

#should print 6
print(grow([1, 2, 3]))
#should print 16
print(grow([4, 1, 1, 1, 4]))
#should print 64
print(grow([2, 2, 2, 2, 2, 2]))