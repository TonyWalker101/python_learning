#codewars kata => https://www.codewars.com/kata/57a55c8b72292d057b000594/python

def rev(st):
  return " ".join((st.split).reverse)

#tests

#should print 'World Hello'
print(rev('Hello World'))
#should print 'There. Hi'
print(rev('Hi There.'))