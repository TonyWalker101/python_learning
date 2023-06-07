#codewars kata => https://www.codewars.com/kata/53697be005f803751e0015aa
vowels = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}
vowel_codes = {"1": "a", "2": "e", "3": "i", "4": "o", "5": "u"}

def encode(st):
  results = ""
  for letter in st:
    if letter in vowels:
      results += vowels[letter]
    else:
      results += letter

  return results
    
def decode(st):
  results = ""
  for letter in st:
    if letter in vowel_codes:
      results += vowel_codes[letter]
    else:
      results += letter

  return results

#tests

#should print 'h2ll4'
print(encode('hello'))
#should print 'H4w 1r2 y45 t4d1y?'
print(encode('How are you today?'))
#should print 'Th3s 3s 1n 2nc4d3ng t2st.'
print(encode('This is an encoding test.'))
#should print 'hello'
print(decode('h2ll4'))