#codewars kata => https://www.codewars.com/kata/550498447451fbbd7600041c/train/python

import math

def comp(array1, array2):
  
  if not array1 or not array2:
    return False
  
  lookup_arr = list(map(lambda x: float(x), array1))

  for num in array2:
    if math.sqrt(num) in lookup_arr:
      lookup_arr.remove(math.sqrt(num)) 
    else:
      return False
  
  return True

#tests

#should print True
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2))
#should print False
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2))
#should print False
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2))