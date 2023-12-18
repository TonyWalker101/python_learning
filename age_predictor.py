#codewars kata => https://www.codewars.com/kata/5aff237c578a14752d0035ae/python

import math

def predict_age(ages):
  sum = 0

  for num in ages:
    sum += num * num

  return math.floor((math.sqrt(sum))/2)

#tests

#should print 86
print(predict_age([65,60,75,55,60,63,64,45]))