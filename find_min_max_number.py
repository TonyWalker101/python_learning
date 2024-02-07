#codewars kata => https://www.codewars.com/kata/577a98a6ae28071780000989/python

def minimum(arr):
  return min(arr)

def maximum(arr):
  return max(arr)

#min tests

#should print -110
print(minimum([-52, 56, 30, 29, -54, 0, -110]))
#should print 0
print(minimum([42, 54, 65, 87, 0]))
#should print 1
print(minimum([1, 2, 3, 4, 5, 10]))

#max tests

#should print 5
print(maximum([5]))
#should print 555
print(maximum([534,43,2,1,3,4,5,5,443,443,555,555]))
#should print 9
print(maximum([9]))