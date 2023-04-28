#kata to return largest possible divisor given two nums

def max_multiple(x,y):
  answer = []
  for i in range(1, y+1):
    if i % x == 0:
      answer.append(i)
  
  return max(answer)

#tests

#should print 6
print(max_multiple(2,7))
#should print 9
print(max_multiple(3,10))
#should print 14
print(max_multiple(7,17))
#should print 50
print(max_multiple(10,50))
#should print 185
print(max_multiple(37,200))
#should print 98
print(max_multiple(7,100))