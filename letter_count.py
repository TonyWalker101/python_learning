#codewars kata => https://www.codewars.com/kata/5865918c6b569962950002a1/python

def str_count(strng, letter):
  return strng.count(letter)

#tests

#should print 2
print(str_count('hello', 'l'))
#should print 1
print(str_count('hello', 'e'))
#should print 1
print(str_count('codewars', 'c'))
#should print 5
print(str_count('ggggg', 'g'))
#should print 2
print(str_count('hello world', 'o'))
#should print 0
print(str_count('', 'z'))