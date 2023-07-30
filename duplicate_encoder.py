#codewars kata => https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/python

from collections import Counter

def duplicate_encode(word):
  word_count = Counter(word.lower())
  results = ""

  for letter in word.lower():
    for key,val in word_count.items():
      if letter == key and val > 1:
        results += ")"
      if letter == key and val == 1:
        results += "("

  return results

#tests

#should print "((("
print(duplicate_encode("din"))
#should print "()()()"
print(duplicate_encode("recede"))
#should print ")())())"
print(duplicate_encode("Success"))
#should print "))(("
print(duplicate_encode("(( @"))
