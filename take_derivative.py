#codewars kata => https://www.codewars.com/kata/5963c18ecb97be020b0000a2/python

def derive(coefficient, exponent): 
  return (str(coefficient*exponent)+"x^"+str(exponent-1))

#tests

#should print "56x^7"
print(derive(7,8))
#should print 45x^8"
print(derive(5,9))