#kata to sum between two integers

def get_sum(a,b):
  
  return sum(range(min(a,b), max(a,b)+1))

#tests

#should print 1
print(get_sum(0,1))
#should print -1
print(get_sum(0,-1))