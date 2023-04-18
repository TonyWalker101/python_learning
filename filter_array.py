#kata to find and return number from a string

def filter_string(string):
  answer = ""

  for letter in string:
    if isinstance( int(letter),(int,float)):
      answer += letter
  
  return int(answer)