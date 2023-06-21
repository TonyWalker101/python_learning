#codewars kata => https://www.codewars.com/kata/5d41e16d8bad42002208fe1a

def more_zeros(s):
  results = []

  for char in s:
    if str(bin(ord(char))).count("0") > str(bin(ord(char))).count("1") and char not in results:
      results.append(char)
  
  return results

#tests

#should print ['a', 'b', 'd']
print(more_zeros('abcde'))
#should print ['h', 'b', 'p', 'a', 'd']
print(more_zeros('thequickbrownfoxjumpsoverthelazydog'))
#should print ['T', 'H', 'E', 'Q', 'I', 'C', 'B', 'R', 'F', 'X', 'J', 'P', 'L', 'A', 'D']
print(more_zeros('THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'))
#should print ['a', 'b', 'd', 'h', 'p', 'A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'L', 'P', 'Q', 'R', 'T', 'X', '0']
print(more_zeros('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'))
#should print ['D', 'I', 'E', 'T']
print(more_zeros('DIGEST'))