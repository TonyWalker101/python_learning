#codewars kata => https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python

def high(x):
  results = []
  #turns string sentence into array
  string_list = x.split(" ")
  
  #calculates score of each word
  for word in string_list:
    total = 0
    for letter in word:
      total += ord(letter.lower()) - 96
    results.append(total)
  
  #gets index of max scoring word
  max_score = results.index(max(results))
  
  return string_list[max_score]
      

#tests

#should print 'taxi'
print(high('man i need a taxi up to ubud'))
#should print 'volcano'
print(high('what time are we climbing up the volcano'))
#should print 'semynak'
print(high('take me to semynak'))
#should print 'aa'
print(high('aa b'))
#should print 'b'
print(high('b aa'))
#should print 'bb'
print(high('bb d'))
#should print 'd'
print(high('d bb'))
#should print "aaa"
print(high("aaa b"))