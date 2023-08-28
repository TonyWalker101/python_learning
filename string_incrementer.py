#codewars kata => https://www.codewars.com/kata/54a91a4883a7de5d7800009c/python

import re

def increment_string(strng):
  m = re.match('^(.*?)(\d+)$', strng)
  name, num = (m.group(1), m.group(2)) if m else (strng, '0')
  return '{0}{1:0{2}}'.format(name, int(num)+1, len(num))

#tests

#should print "foo1"
print(increment_string("foo"))
#should print "foobar002"
print(increment_string("foobar001"))
#should print "foobar2"
print(increment_string("foobar1"))
#should print "foobar01"
print(increment_string("foobar00"))
#should print "foobar100"
print(increment_string("foobar99"))
#should print "foobar100"
print(increment_string("foobar099"))
#should print "fo99obar100"
print(increment_string("fo99obar99"))
#should print 1
print(increment_string(""))