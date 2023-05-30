#codewards kata => https://www.codewars.com/kata/5266876b8f4bf2da9b000362/python

def likes(names):
  if len(names) == 0:
    return "no one likes this"
  elif len(names) == 1:
    return "{} likes this".format(*names)
  elif len(names) < 3:
    return "{} and {} like this".format(*names)
  elif len(names) < 4:
    return "{}, {} and {} like this".format(*names)
  else:
    return "{}, {} and {} others like this".format(names[0], names[1], len(names)-2)

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