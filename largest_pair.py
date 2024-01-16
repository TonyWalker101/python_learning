#codewars kata => https://www.codewars.com/kata/556196a6091a7e7f58000018/python

def largest_pair_sum(numbers): 
  first_largest = max(numbers)
  numbers.remove(first_largest)
  second_largest = max(numbers)

  return first_largest + second_largest

#tests

#should print 42
print(largest_pair_sum([10,14,2,23,19]))
#should print 0
print(largest_pair_sum([-100,-29,-24,-19,19]))
#should print 10
print(largest_pair_sum([1,2,3,4,6,-1,2]))
#should print -18
print(largest_pair_sum([-10, -8, -16, -18, -19]))
