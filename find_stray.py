#codewars kata => https://www.codewars.com/kata/57f609022f4d534f05000024/python

def stray(arr):
  for element in arr:
    if arr.count(element) == 1:
      return element
  
#tests

#should print 2
print(stray([1, 1, 1, 1, 1, 1, 2]))
#should print 3
print(stray([2, 3, 2, 2, 2]))
#should print 3
print(stray([3, 2, 2, 2, 2]))

