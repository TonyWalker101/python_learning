#codewars kata => https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python

def create_phone_number(n):

  #original solution

  ''' phone_number = "("
  count = 0

  def add_to_phone_number():
    nonlocal phone_number
    nonlocal count

    phone_number += str(n[count])
    count += 1
    return

  while count < 3:
    add_to_phone_number()
  
  phone_number += ") "

  while count < 6:
    add_to_phone_number()
  
  phone_number += "-"

  while count < len(n):
    add_to_phone_number()
  
  return phone_number'''

  #refactored solution
  return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

#tests

#should print "(123) 456-7890"
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
#should print "(111) 111-1111"
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
#should print "(123) 456-7890"
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
#should print "(023) 056-0890"
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))
#should print "(000) 000-0000"
print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))