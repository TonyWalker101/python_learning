#codewars kata => https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python

#original solution
'''def wave(people):
  results = []

  if not len(people):
    return results
  
  for x in range(len(people)):
    if people[x] == " ":
      continue
    wave_word = ""
    wave_word += people[:x] + people[x].upper() + people[x+1:]
    results.append(wave_word)
  
  return results'''

#refactored solution
def wave(string):
  return [string[:i] + string[i].upper() + string[i+1:] for i in range(len(string)) if string[i].isalpha()]


#tests

#should print ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
print(wave("hello"))
#should print ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
print(wave("codewars"))
#should print []
print(wave(""))
#should print["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
print(wave("two words"))