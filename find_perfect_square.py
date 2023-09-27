#codewars kata => https://www.codewars.com/kata/56269eb78ad2e4ced1000013/python

def find_next_square(sq):
  x = sq**0.5
  return -1 if x % 1 else (x+1)**2

#tests

#should print 144
print(find_next_square(121))
#should print 676
print(find_next_square(625))
#should print 320356
print(find_next_square(319225))
#should print 15241630849
print(find_next_square(15241383936))
#should print -1
print(find_next_square(3))