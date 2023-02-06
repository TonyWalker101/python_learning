# function to appreciate len()

def get_length(word):
  answer = 0
  for letters in word:
    answer += 1
  
  return answer

# tests

# should print 5
print(len("Hello"))
# should print 5
print(get_length("Hello"))