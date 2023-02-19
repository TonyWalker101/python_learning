#program to update traffic lights to next option

def update_light(current):
  if current == "green":
    return "yellow"
  elif current =="yellow":
    return "red"
  return "green"

#tests

#should print 'yellow'
print(update_light('green'))
#should print 'red'
print(update_light('yellow'))
#should print 'green'
print(update_light('red'))