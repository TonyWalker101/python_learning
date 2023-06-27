#codewars kata => https://www.codewars.com/kata/55a70521798b14d4750000a4/python

def greet(name):
  return "Hello, {} how are you doing today?".format(name)

#tests

#should print "Hello, Ryan how are you doing today?"
print(greet('Ryan'))
#should print "Hello, Shingles how are you doing today?"
print(greet('Shingles'))