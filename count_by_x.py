# function that returns a list of the first n multiples of x

def count_by(x, n):
  return [num*x for num in range(1,n+1)]

# tests

#should return [1, 2, 3, 4, 5]
print(count_by(1, 5))
#should return [2, 4, 6, 8, 10]
print(count_by(2, 5))
#should return [3, 6, 9, 12, 15]
print(count_by(3, 5))
