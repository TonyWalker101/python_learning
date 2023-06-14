#codewars kata => https://www.codewars.com/kata/583af10620dda4da270000c5

def mergeArrays(a, b):
  longer_length = len(a) if len(a) > len(b) else len(b)
  results = []
  
  for i in range(longer_length):
    try:
      results.append(a[i])
      results.append(b[i])
    except:
      continue

  return results      

#tests

#should print [1, "a", 2, "b", 3, "c", 4, "d", 5, "e", 6, 7, 8]
print(mergeArrays([1, 2, 3, 4, 5, 6, 7, 8], ['a', 'b', 'c', 'd', 'e']))
#should print ['a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5]
print(mergeArrays(['a', 'b', 'c', 'd', 'e'], [1, 2, 3, 4, 5]))
#should print [2, 'b', 5, 'r', 8, 'a', 23, 'u', 67, 'r', 6, 's']
print(mergeArrays([2, 5, 8, 23, 67, 6], ['b', 'r', 'a', 'u', 'r', 's']))
#should print ['b', 2, 'r', 5, 'a', 8, 'u', 23, 'r', 67, 's', 6, 'e', 'q', 'z']
print(mergeArrays(['b', 'r', 'a', 'u', 'r', 's', 'e', 'q', 'z'], [2, 5, 8, 23, 67, 6]))