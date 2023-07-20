#codewars kata => https://www.codewars.com/kata/586f6741c66d18c22800010a/python

def sequence_sum(begin_number, end_number, step):
  return sum(range(begin_number, end_number+1, step))

#tests

#should print 12
print(sequence_sum(2, 6, 2))
#should print 15
print(sequence_sum(1, 5, 1))
#should print 5
print(sequence_sum(1, 5, 3))
#should print 45
print(sequence_sum(0, 15, 3))
#should print 0
print(sequence_sum(16, 15, 3))
#should print 26
print(sequence_sum(2, 24, 22))
#should print 2
print(sequence_sum(2, 2, 2))
#should print 2
print(sequence_sum(2, 2, 1))
#should print 35
print(sequence_sum(1, 15, 3))
#should print 0
print(sequence_sum(15, 1, 3))
