#codewars kata => https://www.codewars.com/kata/585d7d5adb20cf33cb000235/python

from collections import Counter

def find_uniq(arr):
  counted_arr = Counter(arr)
  print(counted_arr)
  
  # return "".join([x for x in counted_arr if x == 1])

#tests

#should print 2
print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
#should print 0.55
print(find_uniq([ 0, 0, 0.55, 0, 0 ]))
#should print 10
print(find_uniq([ 3, 10, 3, 3, 3 ]))