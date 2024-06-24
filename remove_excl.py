#codewars kata => https://www.codewars.com/kata/57faf7275c991027af000679/train/python

def remove(st, n):
  return st.replace("!","",n)

#tests

#should print "Hi"
print(remove("Hi!",1))
#should print "Hi"
print(remove("Hi!",100))
#should print "Hi"!!
print(remove("Hi!!!",1))
#should print "Hi"
print(remove("Hi!!!",100))