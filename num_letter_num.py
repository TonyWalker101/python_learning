#codewars kata => https://www.codewars.com/kata/599febdc3f64cd21d8000117/train/python

def numbers_of_letters(n):
  list_num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  results = []
  pre_total = ""

  #step 1: converting initial arg to 'written number'
  for digit in str(n):
    pre_total += list_num[int(digit)]
    
  results.append(pre_total)

  #step 2: filling 2nd element in results list
  results.append(list_num[len(results[0])])

  return results

#should print ["one", "three", "five", "four"
print(numbers_of_letters(1))
#should print ["onetwo", "six", "three", "five", "four"]
print(numbers_of_letters(12))
#should print ["threeseven", "onezero", "seven", "five", "four"]
print(numbers_of_letters(37))
#should print ['threeoneone', 'oneone', 'six', 'three', 'five', 'four']
print(numbers_of_letters(311))
#should print ["nineninenine", "onetwo", "six", "three", "five", "four"]
print(numbers_of_letters(999))