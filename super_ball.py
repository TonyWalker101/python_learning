#codewars kata => https://www.codewars.com/kata/53f0f358b9cb376eca001079/python

class Ball(object):

  def __init__(self, name = ""):
    self.name = name
    self.ball_type = "super" if self.name == "super" else "regular"

#tests

#should print "regular"
print(Ball().ball_type)
#should print "super"
print(Ball('super').ball_type)