#codewars kata => https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python

def two_sum(lst, target):

  for i in range(len(lst)):
    for j in range(1,len(lst)):
      if lst[i] + lst[j] == target:
        return [i, j]

  return []

#tests

#should print [0,2]
print(sorted(two_sum([1,2,3], 4)))
#should print [1,2]
print(sorted(two_sum([1234,5678,9012], 14690)))
#should print [0,1]
print(sorted(two_sum([2,2,3], 4)))