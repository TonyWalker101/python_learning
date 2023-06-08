#codewars kata => https://www.codewars.com/kata/5208f99aee097e6552000148/python

def solution(s):
  results = ""
  for letter in s:
    if letter.isupper():
      results += " "
    results += letter
  
  return results

#tests

#should print "hello World"
print(solution("helloWorld"))
#should print "camel Case"
print(solution("camelCase"))
#should print "break Camel Case"
print(solution("breakCamelCase"))