#program to return a string w/ duplicate letters

#original solution

# def double_char(s):
#   answer = ""
#   for letter in s:
#     answer += letter*2
#   return answer

#refactored solution

def double_char(s):
  return "".join(letter*2 for letter in s)

#tests

#should return "SSttrriinngg"
print(double_char("String"))
#should return "HHeelllloo  WWoorrlldd"
print(double_char("Hello World"))
#should return "11223344!!__  "
print(double_char("1234!_ "))