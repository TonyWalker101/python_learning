#codewars kata => https://www.codewars.com/kata/54a91a4883a7de5d7800009c/python

def increment_string(strng):
  return strng

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