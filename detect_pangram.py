#codewars kata => https://www.codewars.com/kata/545cedaa9943f7fe7b000048/python
from collections import Counter

def is_pangram(s):
  all_letters = Counter(s.lower())
  count = 0

  for key in all_letters.keys():
    if key.isalpha():
      count += 1
  
  if count != 26:
    return False
  
  return True

#tests

#should print True
print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
#should print False
print(is_pangram("1bcdefghijklmnopqrstuvwxyz"))