#codewars kata => https://www.codewars.com/kata/51f9d93b4095e0a7200001b8/python

def how_many_light_sabers_do_you_own(name=""):
  return 18 if name=="Zach" else 0

#tests

#should print 18
print(how_many_light_sabers_do_you_own("Zach"))
#should print 0
print(how_many_light_sabers_do_you_own())
#should print 0
print(how_many_light_sabers_do_you_own("zach"))