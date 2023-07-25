#codewars kata => https://www.codewars.com/kata/54e6533c92449cc251001667/python

def unique_in_order(sequence):
  results = []
  for i in range(len(sequence)):
    if i == 0:
      results.append(sequence[i])
    
    if results[i-1] != sequence[i]:
      results.append(sequence[i])

  return results

#tests

#should print [1, 2, 3, -1]
print(unique_in_order([1, 2, 3, 3, -1]))
#should print ["a", "b", "a"]
print(unique_in_order(["a", "b", "b", "a"]))