#program to update traffic lights to next option

#original solution
# def update_light(current):
#   if current == "green":
#     return "yellow"
#   elif current =="yellow":
#     return "red"
#   return "green"

#refactored solution
def update_light(current):
  return {"green": "yellow", "yellow": "red", "red": "green"}[current]

#tests

#should print 'yellow'
print(update_light('green'))
#should print 'red'
print(update_light('yellow'))
#should print 'green'
print(update_light('red'))