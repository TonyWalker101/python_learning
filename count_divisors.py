#kata to count the # of divisors for a given num

def divisors(num):
  answer = 0
  for x in range(1, num+1):
    if num % x == 0:
      answer += 1
  
  return answer

#tests

#should print 1
print(divisors(1)) 
#should print 3
print(divisors(4))
#should print 2
print(divisors(5))
#should print 6
print(divisors(12))
#should print 8
print(divisors(30))
#should print 13
print(divisors(4096))