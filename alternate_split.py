#codewars kata => https://www.codewars.com/kata/57814d79a56c88e3e0000786/python

def encrypt(text, n):
  if text in ("", None):
    return text
  
  ndx = len(text) // 2

  for i in range(n):
      a = text[:ndx]
      b = text[ndx:]
      text = "".join(b[i:i+1] + a[i:i+1] for i in range(ndx + 1))
  return text


#tests

#tests

#should print "This is a test!"
print(encrypt("This is a test!", 0))
#should print "hsi  etTi sats!"
print(encrypt("This is a test!", 1))
#should print "s eT ashi tist!"
print(encrypt("This is a test!", 2))
#should print " Tah itse sits!"
print(encrypt("This is a test!", 3))
#should print "This is a test!"
print(encrypt("This is a test!", 4))
#should print "This is a test!"
print(encrypt("This is a test!", -1))