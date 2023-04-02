#guided project to practice using sqlite3 and databases w/ python

# Import module 
import sqlite3


# Task 1: Create connection object
con = sqlite3.connect("hotel_booking.db") 

# Task 2: Create cursor object
cur = con.cursor()

# Task 3: View first row of booking_summary
# first_row = cur.execute('''SELECT * FROM booking_summary ''').fetchone()
# print(first_row)

# Task 4: View first ten rows of booking_summary 
# many_row = cur.execute('''SELECT * FROM booking_summary ''').fetchmany(10)
# print(many_row)

# Task 5: Create object bra and print first 5 rows to view data
bra = cur.execute('''SELECT * FROM booking_summary WHERE country = "BRA" ''').fetchall()
# print(bra)
# iter_bra = iter(bra)
# print(next(iter_bra))
# print(next(iter_bra))
# print(next(iter_bra))
# print(next(iter_bra))
# print(next(iter_bra))
# Task 6: Create new table called bra_customers
cur.execute('''CREATE TABLE IF NOT EXISTS bra_customers (
  num INTEGER, 
  hotel TEXT, 
  is_cancelled INTEGER, 
  lead_time INTEGER, 
  arrival_date_year INTEGER, 
  arrival_date_month TEXT, 
  arrival_date_day_of_month INTEGER, 
  adults INTEGER, 
  children INTEGER, 
  country TEXT, 
  adr REAL, 
  special_requests INTEGER)''')

# Task 7: Insert the object bra into the table bra_customers 
cur.executemany('''INSERT INTO bra_customers VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', bra)

# Task 8: View the first 10 rows of bra_customers
bra_customers = cur.execute('''SELECT * FROM bra_customers''').fetchmany(10)
print(bra_customers)

# Task 9: Retrieve lead_time rows where the bookings were canceled

lead_time_can = cur.execute('''SELECT lead_time FROM bra_customers WHERE is_cancelled == 1''').fetchall()

# Task 10: Find average lead time for those who canceled and print results
def calc_average(lst):
  sum = 0
  for x in lst:
    sum += x[0]
  average = sum/len(lst)
  return average

lead_time_can_avg = calc_average(lead_time_can)
print("lead time avg cancelled: ", lead_time_can_avg)

# Task 11: Retrieve lead_time rows where the bookings were not canceled

lead_time = cur.execute('''SELECT lead_time FROM bra_customers WHERE is_cancelled == 0''').fetchall()

# Task 12: Find average lead time for those who did not cancel and print results
lead_time_avg = calc_average(lead_time)
print("lead time avg non-cancelled: ", lead_time_avg)

# Task 13: Retrieve special_requests rows where the bookings were canceled
special_requests_can = cur.execute('''SELECT special_requests FROM bra_customers WHERE is_cancelled == 1''').fetchall()

# Task 14: Find total speacial requests for those who canceled and print results
def count_special_requests(lst):
  count = 0
  for x in lst:
    count += 1
  return count

special_requests_can = count_special_requests(special_requests_can)

print(special_requests_can)

# Task 15: Retrieve special_requests rows where the bookings were not canceled
special_requests_not_can = cur.execute('''SELECT special_requests FROM bra_customers WHERE is_cancelled == 0''').fetchall()

# Task 16: Find total speacial requests for those who did not cancel and print results

special_requests_not_can = count_special_requests(special_requests_not_can)

print(special_requests_not_can)

# Task 17: Commit changes and close the connection
con.commit()
con.close()