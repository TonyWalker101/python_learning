#codewars kata => https://www.codewars.com/kata/570a6a46455d08ff8d001002/python

def no_boring_zeros(n):
  m = str(n)

  if len(m) == 1:
    return m
  
  while m[-1] == "0":
    m = m[:-1]
  
  return m

#tests

#should print 145
print(no_boring_zeros(1450))
#should print 96
print(no_boring_zeros(960000))
#should print 105
print(no_boring_zeros(1050))
#should print -105
print(no_boring_zeros(-1050))
#should print 0
print(no_boring_zeros(0))
#should print 2016
print(no_boring_zeros(2016))