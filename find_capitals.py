#kata to find the capitals in a given string
def capitals(word):
  # answer = []
  # def find_index(lst, lst2):
  #   for x in lst:
  #     answer.

  answer_list = filter(lambda x: x.upper() == x, word)
  # answer_map = map(lambda x: for x in answer_list, answer_list)
  return list(answer_list)

#tests

#should print [0,3,4,6]
print( capitals('CodEWaRs'))