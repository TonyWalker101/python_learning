#codewars kata => https://www.codewars.com/kata/524f5125ad9c12894e00003f/python

def remainder(a,b):
  if min(a,b) == 0:
    return None
  if a > b:
    a % b
  else:
    return b % a

#tests

#should print 2
print(remainder(17,5), 'Returned value should be the value left over after dividing as much as possible.')
#should print -20
print(remainder(-60, 340), 'Should handle negative numbers')
#should print None
print(remainder(1, 0), 'Divide by zero should return None')
#should print None
print(remainder(0, 0), 'Divide by zero should return None')