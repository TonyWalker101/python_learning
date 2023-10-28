#codewars kata => https://www.codewars.com/kata/57241e0f440cd279b5000829/python

def sum_mul(n, m):
  results = n
  x = n*n

  if m <= n: 
    return 'INVALID'

  while True:
    results += x
    x *= n

    if x >= m:
      break

  return x

#tests

#should print 'INVALID'
print(sum_mul(0, 0))
#should print 20
print(sum_mul(2, 9))
#should print 'INVALID'
print(sum_mul(4, -7))