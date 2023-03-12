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
    n = yield name
    if n is not None:
      line_data = n.split(",")
      name = line_data[0]
      age = int(line_data[1])
      guests[name] = age
      n = guests[name]


#creates iterator object w/ function generator
guestlist = read_guestlist("guests_for_event_coordinator_py.txt")

#section 1, print first 10 guests
for i in range(10):
  print(next(guestlist))

#section 2, add Jane to guestlist
guestlist.send("Jane, 35")

#section 3, custom loop using next() for all guests in list
while True:
  try:
    print(next(guestlist))
  except:
    break

#section 4
guests_over_21 = (name for name in guests if guests[name] >= 21)

for guest in guests_over_21:
  print(guest)