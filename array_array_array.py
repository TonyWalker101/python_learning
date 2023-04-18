#kata to practice array manipulation

def explode(arr):  
  answer = []
  score = 0
  first_ele = arr[0]
  second_ele = arr[1]
  if isinstance(first_ele, (int,float)) and isinstance(second_ele, (int,float)):
      score = first_ele + second_ele
  elif not isinstance(first_ele, (int,float)) and isinstance(second_ele, (int,float)):
      return 'Void!'
  elif isinstance(first_ele, (int,float)):
      score = first_ele
  else:
      score = second_ele

  for i in range(score+1):
      answer.append([arr])
  
  return answer

#tests

#should print [[9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3], [9, 3]]
print(explode([9, 3]))
#should print [['a', 3], ['a', 3], ['a', 3]] 
print(explode(['a', 3])) 
#should print [[6, 'c'], [6, 'c'], [6, 'c'], [6, 'c'], [6, 'c'], [6, 'c']]
print(explode([6, 'c'])) 
#should print 'Void!'
print(explode(['a', 'b'])) 
#should print [[1,0]]
print(explode([1, 0])) 
#should print []
print(explode(["a", 0]))
