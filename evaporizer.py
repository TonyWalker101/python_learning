#codewars kata => https://www.codewars.com/kata/5506b230a11c0aeab3000c1f/python

def evaporator(content, evap_per_day, threshold):
	n = 0
	current = 100
	percent = 1 - evap_per_day / 100.0
	while current > threshold:
			current *= percent
			n += 1
	return n

#tests

#should print 22
print(evaporator(10, 10, 10))
#should print 29
print(evaporator(10, 10, 5))
#should print 59
print(evaporator(100, 5, 5))
#should print 37
print(evaporator(50, 12, 1))
      