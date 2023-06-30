#codewars kata => https://www.codewars.com/kata/57fae964d80daa229d000126/python

def remove(s):
  pass

#tests

tests = [
  #[input, [expected]],
  ["Hi!", "Hi"],
  ["Hi!!!","Hi!!"],
  ["!Hi", "!Hi"],
  ["!Hi!", "!Hi"],
  ["Hi! Hi!", "Hi! Hi"],
  ["Hi", "Hi"],
]

for inp, exp in tests:
  print(remove(inp), exp)