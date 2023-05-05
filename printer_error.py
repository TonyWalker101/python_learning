#codewars kata => https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

def printer_error(string):
  numerator = 0
  denominator = len(string)
  
  for x in string:
    if ord(x) not in range(ord("a"), ord("m")+1):
      numerator += 1
  
  return f"{numerator}/{denominator}"

#tests

#should print 3/56
s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
print(printer_error(s))
#should print 6/60
s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
print(printer_error(s))
#should print 11/65
s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
print(printer_error(s))