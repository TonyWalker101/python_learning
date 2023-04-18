#kata to find and return number from a string

def filter_string(string):
  # answer = ""

  # for letter in string:
    
  #   try:
  #     if isinstance(int(letter),(int,float)):
  #       answer += letter
  #   except:
  #     continue
        
  # return int(answer)
  
  return int("".join(filter(str.isdigit, string)))

#tests

#should return 123
print(filter_string("123"))
#should return 123
print(filter_string("a1b2c3"))
#should return 123
print(filter_string("aa1bb2cc3dd"))
#should return 1123
print(filter_string("aa 112 3dd"))
#should return 112233
print(filter_string("11bb2c23c3"))