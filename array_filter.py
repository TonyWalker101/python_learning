#codewars kata => https://www.codewars.com/kata/514a6336889283a3d2000001/python

def get_even_numbers(arr):
  return list(filter(lambda x: x % 2 == 0, arr))

#tests

#should print [2,4,6]
print(get_even_numbers([2,4,5,6]))
#should print []
print(get_even_numbers([]))
#should print []
print(get_even_numbers([1]))
#should print [2]
print(get_even_numbers([1,2]))
#should print  [2,4]
print(get_even_numbers([1,2,3,4,5]))
#should print [2,4,6,8]
print(get_even_numbers([2,4,6,8]))