#program to test if base is a factor of specific num

def check_for_factor(base, factor):
  return True if base % factor == 0 else False

#tests

#should print False
print(check_for_factor(9, 2))
#should print False
print(check_for_factor(653, 7))
#should print False
print(check_for_factor(2453, 5))
#should print False
print(check_for_factor(24617, 3))