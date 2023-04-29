#kata to reverse characters in a string while omitting all non-alphabet characters

def reverse_letter(string):
  answer = ""
  for i in range(len(string)-1, -1, -1):
    if not isinstance(string[i], (int, float)):  
      answer += string[i]
      
  return answer

#tests

#should print "nahsirk"
print(reverse_letter("krishan"))
#should print "nortlu"
print(reverse_letter("ultr53o?n"))
#should print "cba"
print(reverse_letter("ab23c"))
#should print "nahsirk"
print(reverse_letter("krish21an"))