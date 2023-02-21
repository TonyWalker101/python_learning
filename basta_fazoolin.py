#program to practice manipulating Classes

from datetime import time

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return f"The {self.name} menu is available from {self.start_time} to {self.end_time}."
  
  #purchased_items must be a list
  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      total += self.items.get(item)
    return total

class Franchise: 
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return f"This franchise is located at {self.address}."
  
  #hour is in string format
  def available_menus(self, hour):
    available_menus = []
    for menu in self.menus:
      if menu.start_time <= time.fromisoformat(hour) < menu.end_time:
        available_menus.append(menu)
    return available_menus

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises


#creating Menus
brunch = Menu("Brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, time(11), time(16))

early_bird = Menu("Early Bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, time(15), time(18))

dinner = Menu("Dinner", {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, time(17), time(23))

kids = Menu("Kids", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, time(11), time(21))

#testing repr Menu method
# print(brunch)

#testing calculate_bill() method
# print("Brunch total: $", brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
# print("Early Bird total: $", early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

#creating Franchises
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

#testing repr Franchise method
# print(flagship_store)

#testing available_menus() method
# print(flagship_store.available_menus("12:00"))
# print(flagship_store.available_menus("17:00"))

#creating Businesses
first_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
