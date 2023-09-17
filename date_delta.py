from datetime import date, timedelta

d0 = date(2023,9,17)
d1 = date(2023,12,1)

delta = d1-d0
print("days until Dec 1: ",delta.days)

d0 = date(2023,9,17)
d1 = date(2023,12,31)

delta = d1-d0
print("days until Dec 31: ",delta.days)

d0 = date(2023,9,17)
d1 = date(2023,11,1)

delta = d1-d0
print("days until Nov 1: ",delta.days)

d0 = date(2023,9,17)

delta = d0 + timedelta(days=55)
print("today + 55 days: ",delta)

d0 = date(2023,11,11)
d1 = date(2023,12,31)

delta = d1-d0
print("Nov 11 to Dec 31st: ",delta.days)