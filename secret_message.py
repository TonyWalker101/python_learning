#codewars kata => https://www.codewars.com/kata/54808e45ab03a2c8330009fb

import string
def find_secret_message(paragraph):
  paragraph_list = paragraph.split()
  print(paragraph_list)
  results = []

  for word in paragraph_list:
    formatted_word = word.translate(str.maketrans("", "", string.punctuation))
    if formatted_word.lower() not in results:
      results.append(formatted_word.lower())
  
  return " ".join(results)

#tests

#should print 'this test is'
paragraph = 'This is a test. this test is fun.'
print(find_secret_message(paragraph))
#should print 'zxcv asdf qwer'
paragraph = 'asdf qwer zxcv. zxcv fdsa rewq. qazw asdf sxed. qwer crfv.'
print(find_secret_message(paragraph))
