#codewars kata => https://www.codewars.com/kata/5a3dd29055519e23ec000074/python

def check_exam(arr1,arr2):
  score = 0

  for x in range(len(arr1)):
    if arr2[x] == arr1[x]:
      score += 4

    elif arr2[x] != arr1[x] and arr2[x] != "":
      score -= 1
  
  return score

#tests

#should print 6
print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))
#should print 7
print(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]))
#should print 16
print(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]))
#should print 0
print(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]))
    