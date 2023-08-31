#codewars kata => https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/python

def distinct(seq):
  #initial solution
  # return list(set(seq))

  #alt solution
  results = []
  for digit in seq:
    if digit not in results:
      results.append(digit)
  
  return results

#tests

#should print [1]
print(distinct([1]))
#should print [1, 2]
print(distinct([1, 2]))
#should print [1, 2]
print(distinct([1, 1, 2]))
#should print [1, 2, 3, 4, 5]
print(distinct([1, 1, 1, 2, 3, 4, 5]))
#should print [1, 2, 3, 4, 5, 6, 7]
print(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]))