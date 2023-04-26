#function that always returns 5 but without using int or number characters
def unusual_five():
  answer = ["l", "m", "f", "a", "o"]
  return len(answer)

#tests

#should print 5
print(unusual_five())