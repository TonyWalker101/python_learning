#codewars kata => https://www.codewars.com/kata/57fae964d80daa229d000126/python

def remove(s):
  return s[:-1] if s and s[-1] == "!" else s

#tests

#Should print Hi
print(remove("Hi!"))
#Should print Hi!!
print(remove("Hi!!!"))
#Should print Hi
print(remove("Hi"))
#Should print Hi! Hi
print(remove("Hi! Hi!"))