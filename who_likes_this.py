#codewards kata => https://www.codewars.com/kata/5266876b8f4bf2da9b000362/python

def likes(names):
  pass

#tests

#should print 'no one likes this'
print(likes([]))
#should print 'Peter likes this'
print(likes(['Peter']))
#should print 'Jacob and Alex like this'
print(likes(['Jacob', 'Alex']))
#should print 'Max, John and Mark like this'
print(likes(['Max', 'John', 'Mark']))
#should print 'Alex, Jacob and 2 others like this'
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))