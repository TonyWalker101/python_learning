#codewars kata => https://www.codewars.com/kata/5ba38ba180824a86850000f7

def solve(arr): 
  results = []
  for i in arr[::-1]:
    if i not in results:
      results.append(i)
  return results[::-1]

#tests

#should print [4,6,3]
print(solve([3,4,4,3,6,3]))
#should print [1,2,3]
print(solve([1,2,1,2,1,2,3]))
#should print [1,2,3,4]
print(solve([1,2,3,4]),)
#should print [4,5,2,1]
print(solve([1,1,4,5,1,2,1]))