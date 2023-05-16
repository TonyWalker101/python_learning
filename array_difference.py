#codewars kata => https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

def array_diff(a, b):
  pass

#tests

#should print [2]
print(array_diff([1,2], [1]))
#should print [2,2]
print(array_diff([1,2,2], [1]))
#should print [1]
print(array_diff([1,2,2], [2]))
#should print [1,2,2]
print(array_diff([1,2,2], []))
#should print []
print(array_diff([], [1,2]))
#should print [3]
print(array_diff([1,2,3], [1, 2]))