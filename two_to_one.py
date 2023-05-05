#kata from https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python

def longest(a1, a2):
  answer = []

  for x in a1:
    if x not in answer:
      answer.append(x)

  for y in a2:
    if y not in answer:
      answer.append(y)
  
  answer.sort()
  return "".join(answer)

#tests

#should print "aehrsty"
print(longest("aretheyhere", "yestheyarehere"))
#should print "abcdefghilnoprstu"
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))
#should print "acefghilmnoprstuy"
print(longest("inmanylanguages", "theresapairoffunctions"))