#small program to practice OOP

class School():
  def __init__(self, name, level, number_of_students):
    self.name = name
    self.level = level
    self.number_of_students = number_of_students
  
  def get_name(self):
    return self.name

  def get_level(self):
    return self.level
  
  def get_number_of_students(self):
    return self.number_of_students
  
  def set_number_of_students(self, new_number):
    if int(new_number):
      self.number_of_students = new_number
  
  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.number_of_students} students"

#testing School class
