#codewars kata => https://www.codewars.com/kata/56269eb78ad2e4ced1000013/python

from math import sqrt

def find_next_square(sq):
  if not int(sqrt(sq)):
    return -1
  else:
    return 0

#tests

#should print 144
print(find_next_square(121))
#should print 676
print(find_next_square(625))
#should print 320356
print(find_next_square(319225))
#should print 15241630849
print(find_next_square(15241383936))