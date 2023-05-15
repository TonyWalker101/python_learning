# codewars kata => https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python

def expanded_form(num):
  string = list()
  length = len(str(num)) - 1

  for char in str(num):
    if char != "0":
      string.append(char + length * "0")
      length -= 1
  
  return " + ".join(string)

#tests

#should print '10 + 2'
print(expanded_form(12))
#should print '40 + 2'
print(expanded_form(42))
#should print '70000 + 300 + 4'
print(expanded_form(70304))