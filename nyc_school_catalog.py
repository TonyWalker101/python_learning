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
    if isinstance(new_number, int):
      self.number_of_students = new_number
      return
    else:
      return TypeError
  
  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.number_of_students} students"

#testing School class

# willingdon = School("Willingdon", "primary", 200)
# print(willingdon)
# print(willingdon.get_name())
# print(willingdon.get_level())
# print(willingdon.get_number_of_students())
# willingdon.set_number_of_students(250)
# print(willingdon.set_number_of_students("Two Hundred and Fifty"))
# print(willingdon.get_number_of_students())
# print(willingdon)

class PrimarySchool(School):
  def __init__(self, name, number_of_students, pickup_policy):
    super().__init__(name, "primary", number_of_students)
    self.pickup_policy = pickup_policy
  
  def get_pickup_policy(self):
    return self.pickup_policy
  
  def __repr__(self):
    return super().__repr__() + f" and the pick up policy is {self.pickup_policy}"

#testing PrimarySchool class
# primary_school = PrimarySchool("Great School", 150, "before 4 pm")
# print(primary_school)
# print(primary_school.get_pickup_policy())
# print(primary_school.get_name())

class HighSchool(School):
  def __init__(self, name, number_of_students, sports_teams):
    super().__init__(name, "high", number_of_students)
    self.sports_teams = sports_teams
  
  def get_sports_teams(self):
    return self.sports_teams
  
  def __repr__(self):
    return super().__repr__() + f" that has the following sports teams: {self.sports_teams}"
  
#testing HighSchool class
# royalvale = HighSchool("Royal Vale", 500, ["Basketball", "Squash", "Soccer"])
# print(royalvale)
# print(royalvale.get_sports_teams())