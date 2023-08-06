#codewars kata => https://www.codewars.com/kata/545a4c5a61aa4c6916000755/train/python

def gimme(inputArray):
  return inputArray.index(sorted(inputArray)[1])

#tests

#should print 0
print(gimme([2, 3, 1]))
#should print 1
print(gimme([5, 10, 14]))