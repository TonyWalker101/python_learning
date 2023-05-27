#codewars kata => https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/python

from collections import Counter

def duplicate_count(text):
  text_formatted = Counter(text.lower())
  results = [letter for letter,count in text_formatted.items() if count > 1]
  
  return len(results)

#tests

#should print 0 
print(duplicate_count(""))
#should print 0
print(duplicate_count("abcde"))
#should print 1
print(duplicate_count("abcdeaa"))
#should print 2
print(duplicate_count("abcdeaB"))
#should print 2
print(duplicate_count("Indivisibilities"))