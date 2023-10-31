#codewars kata => https://www.codewars.com/kata/5202ef17a402dd033c000009/python

def title_case(title, minor_words=''):
  lst_words = title.split(" ")
  exc_words = list(map(lambda x: x.lower(), minor_words.split(" ")))
  results = ""
  print(exc_words)
  
  for word in lst_words:
    if word.lower() not in exc_words or lst_words.index(word) == 0:
      results += word.title()
    else:
      results += word.lower()
    
    results += " "

  return results.strip()
#tests

#should print ''
print(title_case(''))
#should print 'A Clash of Kings'
print(title_case('a clash of KINGS', 'a an the of'))
#should print 'The Wind in the Willows'
print(title_case('THE WIND IN THE WILLOWS', 'The In'))
#should print 'The Quick Brown Fox'
print(title_case('the quick brown fox'))