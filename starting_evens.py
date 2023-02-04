# program to remove starting even numbers from a list

def delete_starting_evens(lst):
  answer = []
  for i in range(0,len(lst)-1):
    if lst[i] % 2 == 0:
      i += 1
    else:
      answer = lst[i:]
  return answer

#tests

# should print [11, 12, 15]
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
# should print []
print(delete_starting_evens([4, 8, 10]))