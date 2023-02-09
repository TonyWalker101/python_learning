# solution to a "finding a needle in a haystack" problem

def find_needle(haystack):
  for i in range(0, len(haystack)):
    if haystack[i] == 'needle':
      return 'found the needle at position {i}'.format(i=i)

# tests



