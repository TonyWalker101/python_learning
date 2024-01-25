#codewars kata => https://www.codewars.com/kata/57a4d500e298a7952100035d/python

def hex_to_dec(s):
  return int(s, 16)

#tests

#should print 1
print(hex_to_dec("1"))
#should print 10
print(hex_to_dec("a"))
#should print 16
print(hex_to_dec("10"))
