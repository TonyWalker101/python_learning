#program to practice python iterator protocol manipulation
import itertools

student_roster = [
  {
    "name": "Karina M",
    "age": 8,
    "height": 48,
    "favorite_subject": "Math",
    "favorite_animal": "Dog"
  },
  {
    "name": "Yori K",
    "age": 7,
    "height": 50,
    "favorite_subject": "Art",
    "favorite_animal": "Cat"
  },
  {
    "name": "Alex C",
    "age": 7,
    "height": 47,
    "favorite_subject": "Science",
    "favorite_animal": "Cow"
  },
  {
    "name": "Esmeralda R",
    "age": 8,
    "height": 52,
    "favorite_subject": "History",
    "favorite_animal": "Rabbit"
  },
  {
    "name": "Sandy P",
    "age": 7,
    "height": 49,
    "favorite_subject": "Recess",
    "favorite_animal": "Guinea Pig"
  },
  {
    "name": "Matthew Q",
    "age": 7,
    "height": 46,
    "favorite_subject": "Music",
    "favorite_animal": "Walrus"
  },
  {
    "name": "Trudy B",
    "age": 8,
    "height": 45,
    "favorite_subject": "Science",
    "favorite_animal": "Ladybug"
  },
  {
    "name": "Benny D",
    "age": 7,
    "height": 51,
    "favorite_subject": "Math",
    "favorite_animal": "Ant"
  },
  {
    "name": "Helena L",
    "age": 7,
    "height": 53,
    "favorite_subject": "Art",
    "favorite_animal": "Butterfly"
  },
  {
    "name": "Marisol R",
    "age": 8,
    "height": 50,
    "favorite_subject": "Math",
    "favorite_animal": "Lion"
  }
]

class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)

  def _sort_alphabetically(self,students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students
  
  def __iter__(self):
    self.index = 0
    return self
  
  def __next__(self):
    if self.index >= len(self.sorted_names):
      raise StopIteration
    print(f"Good morning {self.sorted_names[self.index]}!")
    self.index += 1
  
  def classroom_pairings(self):
    classroom_pairings = itertools.combinations(self.sorted_names, 2)
    return list(classroom_pairings) 
  
  def afterschool_program(self):
    list_of_students = itertools.chain(self.get_students_with_subject("Math"), self.get_students_with_subject("Science"))
    afterschool_program_students = itertools.combinations(list_of_students, 4)
    return list(afterschool_program_students)

#section 1

# student_roster_iterator = student_roster.__iter__()

# print(student_roster_iterator.__next__())
# print(student_roster_iterator.__next__())
# print(student_roster_iterator.__next__())
# print(student_roster_iterator.__next__())
# print(student_roster_iterator.__next__())
# print(student_roster_iterator.__next__())
# print(student_roster_iterator.__next__())
# print(student_roster_iterator.__next__())
# print(student_roster_iterator.__next__())
# print(student_roster_iterator.__next__())