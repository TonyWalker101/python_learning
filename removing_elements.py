#codewars kata => https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/python

def remove_every_other(my_list):
  #original solution
  # results = []

  # for i in range(0, len(my_list), 2):
  #   results.append(my_list[i])

  # return results

  #refactored solution
  return [my_list[i] for i in range(0, len(my_list),2)]

#tests

#should print ['Hello', 'Hello Again']
print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
#should print [1, 3, 5, 7, 9]
print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
#should print [[1, 2]]
print(remove_every_other([[1, 2]]))
#should print [['Goodbye']]
print(remove_every_other([['Goodbye'], {'Great': 'Job'}]))