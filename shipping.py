# program to determine the best package-shipping rate possible

weight = 10
cost = 0

# ground shipping
flat_rate = 20.00

if weight <= 2:
  cost = (1.50 * weight) + flat_rate
elif weight <= 6:
  cost = (3.00 * weight) + flat_rate
elif weight <= 10:
  cost = (4.00 * weight) + flat_rate
else:
  cost = (4.75 * weight) + flat_rate










