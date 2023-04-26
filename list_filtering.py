#kata to remove the strings from a given list

def filter_list(lst):
  return [num for num in lst if isinstance(num, (int, float))]

#tests

#should print [1, 2]
print(filter_list([1, 2, 'a', 'b']))
#should print [1, 0, 15]
print(filter_list([1, 'a', 'b', 0, 15]))
#should print [1, 2, 123]
print(filter_list([1, 2, 'aasf', '1', '123', 123]))