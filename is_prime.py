#codewars kata => https://www.codewars.com/kata/5262119038c0985a5b00029f/python

from math import sqrt

def is_prime(num):
  if num < 1:
    return False
  
  i = 2
  while i <= sqrt(num):
    if num % i == 0:
      return False
    i += 1

  return True


#tests

#should print True
print(is_prime(3))
#should print True
print(is_prime(5))
#should print True
print(is_prime(7))
#should print False
print(is_prime(4))
#should print False
print(is_prime(6))
#should print False
print(is_prime(8))