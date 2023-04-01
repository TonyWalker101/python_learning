#program to add line number after each element in list

def number(lines):
    
  return [f"{n}: {lines[n-1]}" for n in range(1, len(lines)+1)]

#tests

#should equal []
print(number([]))

#should equal ["1: a", "2: b", "3: c"]
print(number(["a", "b", "c"]))