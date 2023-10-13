#codewars kata => https://www.codewars.com/kata/545991b4cbae2a5fda000158/python

def include(arr,item):
  return item in arr

#tests

#should print True
print(include([1,2,3,4], 3))
#should print False
print(include([1,2,4,5], 3))