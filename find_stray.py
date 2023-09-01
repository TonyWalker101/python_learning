#codewars kata => https://www.codewars.com/kata/57f609022f4d534f05000024/python

def stray(arr):
  results = arr[0]
  for element in arr[1:]:
    if results != element:
      return element

  return results
#tests

#should print 2
print(stray([1, 1, 1, 1, 1, 1, 2]))
#should print 3
print(stray([2, 3, 2, 2, 2]))
#should print 3
print(stray([3, 2, 2, 2, 2]))

