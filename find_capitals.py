#kata to find the capitals in a given string
def capitals(word):
  def find_index(lst):
    return word.index(lst)

  return list(map(find_index, filter(lambda x: x.upper() == x, word)))

#tests

#should print [0,3,4,6]
print( capitals('CodEWaRs'))