# program to remove starting even numbers from a list

def delete_starting_evens(lst):
  for num in lst:
    if num % 2 == 0:
      lst.remove(num)
      print(f'i\'ve removed {num}')
    else:
      print(f'I\'m not removing {num}')
  return lst

#tests

# should print [11, 12, 15]
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
# should print []
print(delete_starting_evens([4, 8, 10]))