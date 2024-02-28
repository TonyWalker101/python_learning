#codewars kata => https://www.codewars.com/kata/559d2284b5bb6799e9000047/python

def add_length(str_):
  results = []
  string_lst = str_.split()

  for word in string_lst:
    results.append(word+" "+str(len(word)))
  
  return results


#tests

#should print ["apple 5", "ban 3"]
print(add_length('apple ban'))
#should print ["you 3", "will 4", "win 3"]
print(add_length('you will win'))
#should print ["you 3"]
print(add_length('you'))
#should print ["y 1"]
print(add_length('y'))