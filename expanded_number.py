# codewars kata => https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python

def expanded_form(num):
  string_num = str(num)
  results = []

  for i in range(len(string_num)):
    if string_num[i] == 0:
      continue
    elif i == 1:
      results.append(string_num[i])
      continue
    else:
      # num_to_add = string_num[i]
      # count = i
      # while count > 0:
      #   num_to_add += "0"
      #   count -= 1
      # results.append(num_to_add)
      results.append(string_num[i] + ("0" * i))
  
  # results.reverse()

  return " + ".join(results)
      


#tests

#should print '10 + 2'
print(expanded_form(12))
#should print '40 + 2'
print(expanded_form(42))
#should print '70000 + 300 + 4'
print(expanded_form(70304))