#codewars kata => https://www.codewars.com/kata/5966e33c4e686b508700002d/python

def sum_str(a, b):
  if not a and not b:
    return "0"
  elif not a:
    return b
  elif not b:
    return a
  
  results = int(a, base=10) + int(b, base=10)
  return str(results)

#tests

#should print "9"
print(sum_str("5","4"))
#should print "9"
print(sum_str("9",""))
#should print "9"
print(sum_str("","9"))
#should print "0"
print(sum_str("",""))