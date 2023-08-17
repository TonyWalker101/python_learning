#codewars kata => https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

def is_valid_walk(walk):
  return len(walk) == 10

#tests

#should print True
print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
#should print False
print(is_valid_walk(['n']))