#codeswars kata => https://www.codewars.com/kata/576bb71bbbcf0951d5000044/python

def count_positives_sum_negatives(arr):
  return

#tests

#should print [10,-65]
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
#should print [8,-50]
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
#should print [1,0]
print(count_positives_sum_negatives([1]))
#should print [0,-1]
print(count_positives_sum_negatives([-1]))
#should print [0,0]
print(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]))
#should print []
print(count_positives_sum_negatives([]))
