#codewars kata => https://www.codewars.com/kata/54e6533c92449cc251001667/python

def unique_in_order(sequence):
  result = []
  prev = None
  for char in sequence[0:]:
      if char != prev:
          result.append(char)
          prev = char
  return result

#tests

#should print [1, 2, 3, -1]
print(unique_in_order([1, 2, 3, 3, -1]))
#should print ["a", "b", "a"]
print(unique_in_order(["a", "b", "b", "a"]))