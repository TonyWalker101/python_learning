#kata to see if one word is an anagram of the other (https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/python)

def is_anagram(test, original):
  test_word = test.upper()
  if len(test) != len(original):
      return False
  for i in original:
      index = test_word.find(i.upper())
      if index == -1:
          return False
      else:
          test_word.replace(i,"",1)
              
  return True

#should print True
print(is_anagram("foefet", "toffee"))
#should print True
print(is_anagram("Buckethead", "DeathCubeK"))
#should print True
print(is_anagram("Twoo", "WooT"))
#should print False
print(is_anagram("dumble", "bumble"))
#should print False
print(is_anagram("ound", "round"))
#should print False
print(is_anagram("apple", "pale"))