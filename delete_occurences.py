#codewars kata => https://www.codewars.com/kata/554ca54ffa7d91b236000023/python

def delete_nth(order,max_e):
  results = []

  for num in order:
    if results.count(num) < max_e:
      results.append(num)

  return results

#tests

#should print [20,37,21]
print(delete_nth([20,37,20,21], 1))
#should print [1, 1, 3, 3, 7, 2, 2, 2]
print(delete_nth([1,1,3,3,7,2,2,2,2], 3))

