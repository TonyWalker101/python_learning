#codewars kata => https://www.codewars.com/kata/555086d53eac039a2a000083/python

def lovefunc(flower1, flower2):
  return flower1 % 2 == 0 and flower2 % 2 != 0 or flower1 % 2 != 0 and flower2 % 2 == 0

#should print True  
print(lovefunc(1,4))
#should print False
print(lovefunc(2,2))
#should print True
print(lovefunc(0,1))
#should print False
print(lovefunc(0,0))