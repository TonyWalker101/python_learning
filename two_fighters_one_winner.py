#codewars kata => https://www.codewars.com/kata/577bd8d4ae2807c64b00045b/python

class Fighter(object):
  def __init__(self, name, health, damage_per_attack):
      self.name = name
      self.health = health
      self.damage_per_attack = damage_per_attack
      
  def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
  __repr__=__str__

def declare_winner(fighter1, fighter2, first_attacker):
  pass

#tests

#should print "Lew"
print(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew"))
#should print "Harry"
print(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Harry"))
#should print "Harald"
print(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry"))
#should print "Harald"
print(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald"))
#should print "Harald"
print(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"))
#should print "Harald"
print(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald"))
