#codewars kata => https://www.codewars.com/kata/5680781b6b7c2be860000036/train/python

def vowel_indices(word):
  answer = []
  current_index = 0

  for letter in word:
    current_index += 1

    if letter.lower() in ["a","e","i","o","u","y"]:
      answer.append(current_index)
  
  return answer


#tests

#should print []
print(vowel_indices("mmm"))
#should print [1,5]
print(vowel_indices("apple"))
#should print []
print(vowel_indices("123456"))
#should print [1,4,6,9]
print(vowel_indices("UNDISARMED"))