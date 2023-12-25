#codewars kata => https://www.codewars.com/kata/59377c53e66267c8f6000027/python

def alphabet_war(fight):
  left_side = {"w":4,"p":3,"b":2,"s":1,"score":0}
  right_side = {"m":4,"q":3,"d":2,"z":1,"score":0}

  for letter in fight:
    if letter in left_side:
      left_side["score"] += left_side[letter]
    if letter in right_side:
      right_side["score"] += right_side[letter]
    else:
      continue
  
  if left_side["score"] > right_side["score"]:
    return "Left side wins!"
  elif left_side["score"] < right_side["score"]:
    return "Right side wins!"
  else:
    return "Let's fight again!"

#tests

#should print "Right side wins!"
print(alphabet_war("z"))
#should print "Let's fight again!"
print(alphabet_war("zdqmwpbs"))
#should print "Left side wins!"
print(alphabet_war("wq"))
#should print "Right side wins!"
print(alphabet_war("zzzzs"))
#should print "Left side wins!"
print(alphabet_war("wwwwww"))