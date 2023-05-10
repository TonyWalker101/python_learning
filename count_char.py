# codewares kata => https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python

def count(s):
  results = {}
  if not s:
    return results
  
  for letter in s:
    if letter not in results:
      results.update({letter: 1})
    else:
      results[letter] += 1
  
  return results

#tests

#should print {'a': 2, 'b': 1}
print(count('aba'))
#should print {}
print(count(''))
#should print {'a' : 2}
print(count('aa'))
#should print {'b' : 2, 'a' : 2}
print(count('aabb'))