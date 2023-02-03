# program that sums the last two elements of an array and adds the result to the end of the array
def append_sum(my_list):
  count = 0
  while count < 3:
    my_list.append(my_list[-1]+my_list[-2])
    count+=1
  return my_list

# should return [1, 1, 2, 3, 5, 8]
print(append_sum([1, 1, 2]))
