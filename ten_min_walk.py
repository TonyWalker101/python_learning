#codewars kata => https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

def is_valid_walk(walk):
  if (walk.count('n') == walk.count('s') and 
        walk.count('e') == walk.count('w') and
        len(walk) == 10):
            return True
  return False

#tests

#should print True
print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
#should print False
print(is_valid_walk(['n']))