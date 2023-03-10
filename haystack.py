# solution to a "finding a needle in a haystack" problem

# previous solution

# def find_needle(haystack):
#   for i in range(0, len(haystack)):
#     if haystack[i] == 'needle':
#       return 'found the needle at position {i}'.format(i=i)

def find_needle(haystack):
  return f"found the needle at index {haystack.index('needle')}"

# tests

# should return needle at index 3
print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))
# should return needle at index 5
print(find_needle(['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle', 'something somebody lost a while ago']))
# should return needle at index 30
print(find_needle([1,2,3,4,5,6,7,8,8,7,5,4,3,4,5,6,67,5,5,3,3,4,2,34,234,23,4,234,324,324,'needle',1,2,3,4,5,5,6,5,4,32,3,45,54]))



