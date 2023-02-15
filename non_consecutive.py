# program to test if numbers in a list are non-consecutive

def first_non_consecutive(arr):
  start = arr[0]
  for i in range(1, len(arr)):
    if arr[i] - start == 1:
      start = arr[i]
    else: 
      return arr[i]
  return None

# tests

#should print 6
print(first_non_consecutive([1,2,3,4,6,7,8]))
#should print None
print(first_non_consecutive([1,2,3,4,5,6,7,8]))
#should print 6
print(first_non_consecutive([4,6,7,8,9,11]))