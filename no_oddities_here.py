#codewars kata => https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce

def no_odds(values):
  return [x for x in values if x % 2 == 0]

#tests
#should print [0]
print(no_odds([0, 1]))
#should print [0, 2]
print(no_odds([0, 1, 2, 3]))
#should print []
print(no_odds([1, 3, 5, 7, 9]))
#should print [0, 2, 4, 6, 8, 10]
print(no_odds([0, 2, 4, 6, 8, 10]))
#should print []
print(no_odds([-1, -3, -5, -7, -9]))
#should print [2, 4, 8, 6, 0]
print(no_odds([2, 4, 8, 6, 0]))
#should print []
print(no_odds([]))