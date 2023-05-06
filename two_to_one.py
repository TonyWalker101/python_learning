#kata from https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python

def longest(a1, a2):
  
  #original solution

  ''' def count_letters(*args):
    results = []

    for word in args:
      for letter in word:
        if letter not in results:
          results.append(letter)

    results.sort()
    return results

  return "".join(count_letters(a1,a2))'''

  #refactored solution
  
  return "".join(sorted(set(a1+a2)))


#tests

#should print "aehrsty"
print(longest("aretheyhere", "yestheyarehere"))
#should print "abcdefghilnoprstu"
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))
#should print "acefghilmnoprstuy"
print(longest("inmanylanguages", "theresapairoffunctions"))