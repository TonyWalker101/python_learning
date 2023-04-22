#kata to find the capitals in a given string
def capitals(word):
  answer = []
  for x in range(len(word)):
      if word[x] == word[x].upper():
          answer.append(x)
            
  return answer

#tests

#should print [0,3,4,6]
print( capitals('CodEWaRs'))