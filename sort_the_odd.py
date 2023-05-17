#codewards kata => https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python

def sort_array(source_array):
  results = []
  odd_numbers = list(filter(lambda x: x % 2 != 0, source_array))
  odd_numbers.sort()
  count = 0

  for num in source_array:
    if num % 2 == 0:
      results.append(num)
    else:
      results.append(odd_numbers[count])
      count += 1
  
  return results

#tests

#should print [1, 3, 2, 8, 5, 4]
print(sort_array([5, 3, 2, 8, 1, 4]))
#should print [1, 3, 5, 8, 0]
print(sort_array([5, 3, 1, 8, 0]))
#should print []
print(sort_array([]))