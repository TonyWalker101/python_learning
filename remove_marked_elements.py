#codewards kata => https://www.codewars.com/kata/563089b9b7be03472d00002b/train/python

def remove_(integer_list, values_list):
  results = integer_list

  for num in integer_list:
    for value in values_list:
      if num != value:
        break
      else:
        results.remove(num)

  return results

#tests

#should print  [2, 2, 4]
integer_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
values_list = [1, 3]
print(remove_(integer_list, values_list))

#should print [5, 6 ,7 ,8]
integer_list = [1, 1, 2 ,3 ,1 ,2 ,3 ,4, 4, 3 ,5, 6, 7, 2, 8]
values_list  = [1, 3, 4, 2]
print(remove_(integer_list, values_list))

#should print [8, 7, 6, 5, 1]
integer_list = [8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2 , 3]
values_list  = [2, 4, 3]
print(remove_(integer_list, values_list))