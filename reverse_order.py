#codewars kata => https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b/python


def reverse_list(l):
  return l[::-1]

#tests

#should print [4,3,2,1]
print(reverse_list([1,2,3,4]))
#should print [4,5,1,3]
print(reverse_list([3,1,5,4]))
#should print [2,9,6,3]
print(reverse_list([3,6,9,2]))
#should print [1]
print(reverse_list([1]))

