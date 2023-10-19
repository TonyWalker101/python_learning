#codewars kata => https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/python

def open_or_senior(data):
  #initial solution
  results = []
  for lst in data:
    if lst[0] >= 55 and lst[1] > 7:
      results.append("Senior")
    else:
      results.append("Open")
  return results

  #refactored solution
  # return ["Senior" for lst in data if lst[0] >= 55 and lst[1] > 7 else "Open"]÷\

#tests

#should print ['Open', 'Senior', 'Open', 'Senior']
print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))
#should print ['Open', 'Open', 'Senior', 'Open']
print(open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)]))