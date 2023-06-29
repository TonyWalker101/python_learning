#codewars kata => https://www.codewars.com/kata/54808e45ab03a2c8330009fb

import string

def find_secret_message(paragraph):
  word_list = []
  dupe_words = []
  formatted_paragraph = list(map(lambda x: x.lower().translate(str.maketrans("", "", string.punctuation)), paragraph.split()))
  # print(list(formatted_paragraph))

  for word in formatted_paragraph:
    # if formatted_paragraph.count(word) > 1 and word not in results:
    #   results.append(word)
    if word in word_list and word not in dupe_words:
      dupe_words.append(word)

    word_list.append(word)
    
  return " ".join(dupe_words)

#tests

#should print 'this test is'
paragraph = 'This is a test. this test is fun.'
print(find_secret_message(paragraph))
#should print 'zxcv asdf qwer'
paragraph = 'asdf qwer zxcv. zxcv fdsa rewq. qazw asdf sxed. qwer crfv.'
print(find_secret_message(paragraph))
