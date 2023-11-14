#codewars kata => https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e/python
def sum_of_differences(arr):
  return max(arr) - min(arr) if arr else 0

#tests

#should print 9
print(sum_of_differences([1, 2, 10]))
#should print 2
print(sum_of_differences([-3, -2, -1]))
#should print 0
print(sum_of_differences([1, 1, 1, 1, 1]))
#should print 34
print(sum_of_differences([-17, 17]))      
#should print 0
print(sum_of_differences([]))
#should print 0
print(sum_of_differences([0]))
#should print 0
print(sum_of_differences([-1]))
#should print 0
print(sum_of_differences([1]))