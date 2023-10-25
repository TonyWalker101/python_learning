#codewars kata => https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/python

def row_weights(array):
  team_1 = 0
  team_2 = 0

  for x in range(len(array)):
    if x % 2 == 0:
      team_1 += array[x]
    else:
      team_2 += array[x]
  
  return (team_1,team_2)

#tests

#should print (80,0)
print(row_weights([80]))
#should print (100,50)
print(row_weights([100,50]))
#should print (120,140)
print(row_weights([50,60,70,80]))
#should print (62,27)
print(row_weights([13,27,49]))
#should print (236,92)
print(row_weights([70,58,75,34,91]))