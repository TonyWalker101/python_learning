#codewars kata => https://www.codewars.com/kata/528d36d7cc451cd7e4000339/train/python

class Student:
  def __init__(self, name, fives, tens, twenties):
    self.name = name
    self.fives = fives
    self.tens = tens
    self.twenties = twenties

def most_money(students):
  winner_total = 0
  winner_name = ""
  for student in students:
    student_total = student.fives * 5 + student.tens * 10 + student.twenties * 20 
    if student_total == winner_total:
      winner_name = "all"
    elif student_total > winner_total:
      winner_total = student_total
      winner_name = student.name.title()
      
  return winner_name

#tests

phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 0)

#should print "Phil"
print(most_money([cam, geoff, phil]))
#should print "all"
print(most_money([cam, geoff]))
#should print "Geoff"
print(most_money([geoff]))