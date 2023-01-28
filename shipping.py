# program to determine the best package-shipping rate possible

# in lbs
weight = int(input("How much does your package weigh? "))

''' 
standard shipping => premium & drone == False
premium shipping => premium == True, drone == False
drone shipping => premium == False, drone == True
all options => premium & drone == True 
'''
premium = True
drone = True

# static variables, CAD
flat_rate = 20.00
cost_standard = 0
cost_premium = 0
cost_drone= 0

# main functionality
if premium == False and drone == False:
  # ground shipping
  if weight <= 2:
    cost_standard = (1.50 * weight) + flat_rate
  elif weight <= 6:
    cost_standard = (3.00 * weight) + flat_rate
  elif weight <= 10:
    cost_standard = (4.00 * weight) + flat_rate
  else:
    cost_standard = (4.75 * weight) + flat_rate
  print("Standard ground shipping costs: ", round(cost_standard,2),"$")
  # premium group shipping
elif premium == True and drone == False:
  cost_premium = 125.00
  print("Premium ground shipping costs: ", round(cost_premium,2), "$")
  # drone shipping
elif premium == False and drone == True:
  if weight <= 2:
    cost_drone = (4.50 * weight)
  elif weight <= 6:
    cost_drone = (9.00 * weight)
  elif weight <= 10:
    cost_drone = (12.00 * weight)
  else:
    cost_drone = (14.25 * weight)
  print("Drone shipping costs: ", round(cost_drone,2), "$")
# all options for comparison (premium and drone == True)
else:
  # ground standard for comparison
  if weight <= 2:
    cost_standard = (1.50 * weight) + flat_rate
  elif weight <= 6:
    cost_standard = (3.00 * weight) + flat_rate
  elif weight <= 10:
    cost_standard = (4.00 * weight) + flat_rate
  else:
    cost_standard = (4.75 * weight) + flat_rate
  print("Standard ground shipping costs: ", round(cost_standard,2),"$")
  # premium ground for comparison
  cost_premium = 125.00
  print("Premium ground shipping costs: ", round(cost_premium,2), "$")
  # drone for comparison
  if weight <= 2:
    cost_drone = (4.50 * weight)
  elif weight <= 6:
    cost_drone = (9.00 * weight)
  elif weight <= 10:
    cost_drone = (12.00 * weight)
  else:
    cost_drone = (14.25 * weight)
  print("Drone shipping costs: ", round(cost_drone,2), "$")







