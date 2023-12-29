#codewars kata => https://www.codewars.com/kata/58d248c7012397a81800005c/python

def cube_checker(volume, side):
  return 0 < volume == side**3 

#tests

#should print False
print(cube_checker(-12,2))
#should print False
print(cube_checker(8, 3))
#should print True
print(cube_checker(8, 2))