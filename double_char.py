# program to return a string w/ duplicate letters

def double_char(s):
  answer = ""
  for letter in s:
    answer += letter*2
  return answer

#tests

#should return "SSttrriinngg"
print(double_char("String"))
#should return "HHeelllloo  WWoorrlldd"
print(double_char("Hello World"))
#should return "11223344!!__  "
print(double_char("1234!_ "))