#codewars kata => https://www.codewars.com/trainer/python

from collections import Counter

def find_it(seq):
  # seq_count = Counter(seq)
  # return int(" ".join([str(key) for key, val in seq_count.items() if val % 2 != 0]))

  #refactored solution
  for i in seq:
    if seq.count(i) % 2 != 0:
      return i

#should print 5
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))

#should print -1
print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))

#should print 5
print(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]))

#should print 10
print(find_it([10]))

#should print 10
print(find_it([10, 10, 10])) 

#should print 10
print(find_it([1,1,1,1,1,1,10,1,1,1,1]))

#should print 1
print(find_it([5,4,3,2,1,5,4,3,2,10,10]))