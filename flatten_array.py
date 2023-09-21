#codewars kata => https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/python

def flatten_and_sort(arrays):
  # original solution
  # results = []
  # for lst in array:
  #   for element in lst:
  #     results.append(element)
  # return sorted(results)

  # refactored solution
  return sorted([element for array in arrays for element in array])


#tests

#should print []
print(flatten_and_sort([]))
#should print []
print(flatten_and_sort([[], []]))
#should print [1]
print(flatten_and_sort([[], [1]]))
#should print [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]))
#should print [1, 2, 3, 4, 5, 6, 100]
print(flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]]))