#codewars kata => https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/python

def duplicate_encode(word):
  pass

#tests

#should print "((("
print(duplicate_encode("din"))
#should print "()()()"
print(duplicate_encode("recede"))
#should print "should ignore case"
print(duplicate_encode("Success"),")())())")
#should print "))(("
print(duplicate_encode("(( @"))
