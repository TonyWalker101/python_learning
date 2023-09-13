#codewars kata => https://www.codewars.com/kata/559590633066759614000063/python

def min_max(lst):
  return [min(lst), max(lst) if min(lst) != max(lst) else min(lst)]

#tests

#should print [1, 5]
print(min_max([1,2,3,4,5]))
#should print [5, 2334454]
print(min_max([2334454,5]))