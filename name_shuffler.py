#codewars kata => https://www.codewars.com/kata/559ac78160f0be07c200005a/python

def name_shuffler(str_):
  name = str_.split()
  name.reverse()
  return " ".join(name)

#tests

#should print McClane john
print(name_shuffler('john McClane'))
#should print jeggins Mary
print(name_shuffler('Mary jeggins'))
#should print jerry tom
print(name_shuffler('tom jerry'))