#codewars kata => https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/python

from collections import Counter

def duplicate_encode(word):
  #original solution
  # word_count = Counter(word.lower())
  # results = ""

  # for letter in word.lower():
  #   for key,val in word_count.items():
  #     if letter == key and val > 1:
  #       results += ")"
  #     if letter == key and val == 1:
  #       results += "("

  # return results

  #refactored solution
  counter = Counter(word.lower())
  return ''.join(('(' if counter[c] == 1 else ')') for c in word)

#tests

#should print "((("
print(duplicate_encode("din"))
#should print "()()()"
print(duplicate_encode("recede"))
#should print ")())())"
print(duplicate_encode("Success"))
#should print "))(("
print(duplicate_encode("(( @"))
