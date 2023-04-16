#kata to sum between two integers

def get_sum(a,b):
  answer = 0
  start = 0
  end = 0
  
  if a > b:
      start = b
      end = a
  elif a < b:
      start = a
      end = b
  elif a == b:
      return a
      
  for x in range(start,end+1):
      answer += x
      
  return answer
