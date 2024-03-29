#codewars kata => https://www.codewars.com/kata/5202ef17a402dd033c000009/python

def title_case(title, minor_words=''):
  lst_words = title.capitalize().split(" ")
  exc_words = minor_words.lower().split(" ")
  
  return " ".join(word if word in exc_words else word.capitalize() for word in lst_words)

#tests

#should print ''
print(title_case(''))
#should print 'A Clash of Kings'
print(title_case('a clash of KINGS', 'a an the of'))
#should print 'The Wind in the Willows'
print(title_case('THE WIND IN THE WILLOWS', 'The In'))
#should print 'The Quick Brown Fox'
print(title_case('the quick brown fox'))