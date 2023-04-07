#program to return smallest int in list

def find_smallest_int(arr):
  # Code here
  answer = arr[0]
  for i in range(1,len(arr)):
      if arr[i] <= answer:
          answer = arr[i]
          
  return answer

#tests

#should return 11
print(find_smallest_int([78, 56, 232, 12, 11, 43]))
#should return -33
print(find_smallest_int([78, 56, -2, 12, 8, -33]))
#should return -18446744073709551615
print(find_smallest_int([0, 1-2**64, 2**64]))