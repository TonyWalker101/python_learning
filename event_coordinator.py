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

#section 5
def table_1():
  for i in range(1,6):
    yield ("Chicken", "Table 1", f"Seat {i}")

def table_2():
  for i in range(1,6):
    yield ("Beef", "Table 2", f"Seat {i}")

def table_3():
  for i in range(1,6):
    yield ("Fish", "Table 3", f"Seat {i}")

chicken_table = table_1()
beef_table = table_2()
fish_table = table_3()

for seat in chicken_table:
  print(seat)

for seat in beef_table:
  print(seat)

for seat in fish_table:
  print(seat)

#section 6
def guest_to_table(guests_list, table_1_list, table_2_list, table_3_list):
  guests = iter(guests_list)
  tables_1 = table_1_list()
  tables_2 = table_2_list()
  tables_3 = table_3_list()

  for table in tables_1:
    try:
      yield (f"{next(guests)}", table)
    except:
      continue

  for table in tables_2:
    try:
      yield (f"{next(guests)}", table)
    except: 
      continue

  for table in tables_3:
    try:
      yield (f"{next(guests)}", table)
    except:
      continue

tables_to_guests = guest_to_table(guests, table_1, table_2, table_3)

for table_combo in tables_to_guests:
  print(table_combo)