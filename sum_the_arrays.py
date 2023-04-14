#kata to sum int 

def sum(arr):
  answer = 0
  for x in arr:
    answer += x
  
  return answer

#tests

#should return 10
print(sum([1,2,3,4]))
#should return 85
print(sum([10, 28, 14, 33]))