#codewars kata => https://www.codewars.com/kata/57eae65a4321032ce000002d/python

def fake_bin(x):
  results = []
  for num in x:
    if num in ["0","1","2","3","4"]:
      results.append("0")
    else:
      results.append("1")
  return "".join(results)

