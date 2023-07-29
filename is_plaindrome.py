#codewars kata => https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/python

def is_palindrome(s):
  
  #original solution
  # reverse_word = list(s.lower())
  # reverse_word.reverse()

  # if s.lower() == "".join(reverse_word):
  #   return True
  
  # return False

  #refactored solution
  return s.lower() == s.lower()[::-1]

#tests

#should print True
print(is_palindrome('a'))
#should print True
print(is_palindrome('aba'))
#should print True
print(is_palindrome('Abba'))
#should print True
print(is_palindrome('malam'))
#should print False
print(is_palindrome('walter'))
#should print True
print(is_palindrome('kodok'))
#should print False
print(is_palindrome('Kasue'))