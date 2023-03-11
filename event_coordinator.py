#program to practice python function generators

guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  while True:
    line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    yield name

guestlist = read_guestlist("guests_for_event_coordinator_py.txt")
#section 1
for i in range(10):
  print(next(guestlist))

#section 2
guestlist.send("Jane, 35")

#section 3
