#codewars kata => https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8

import re

def remove_parentheses(s):

  while "(" in s:
    s = re.sub("\([^()]*\)", "", s)
  
  return s

#tests

#should print "exampleexample"
print(remove_parentheses("example(unwanted thing)example"))
#should print "example  example"
print(remove_parentheses("example (unwanted thing) example"))
#should print "a e"
print(remove_parentheses("a (bc d)e"))
#should print "a"
print(remove_parentheses("a(b(c))"))
#should print "hello example  something"
print(remove_parentheses("hello example (words(more words) here) something"))
#should print "  "
print(remove_parentheses("(first group) (second group) (third group)"))