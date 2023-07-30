#codewars kata => https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/python

from collections import Counter

def duplicate_encode(word):
  word_count = Counter(word)
  results = ""

  for key,val in word_count.items():
    if val > 1:
      results += "("
    if val == 1:
      results += ")"

  return results

#tests

#should print "((("
print(duplicate_encode("din"))
#should print "()()()"
print(duplicate_encode("recede"))
#should print "should ignore case"
print(duplicate_encode("Success"),")())())")
#should print "))(("
print(duplicate_encode("(( @"))
