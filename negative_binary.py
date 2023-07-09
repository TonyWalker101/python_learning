#codewars kata => https://www.codewars.com/kata/5becace7063291bebf0001d5/python

def positive_to_negative(binary):
  #if binary num = 0, return original binary list
  if binary.count(1) == 0:
    return binary
  
  #inverts (flips) binary nums from binary list
  flipped_binary = list(map(lambda x: 0 if x == 1 else 1, binary))

  #starts loop at end of list
  for i in range(len(flipped_binary)-1,0,-1):
    #add 1 if num is 0, then stop iteration
    if flipped_binary[i] == 0:
      flipped_binary = flipped_binary[:i] + [1] + flipped_binary[i+1:]
      break
    else:
      #if num is 1, make 0 and continue to next num in list
      flipped_binary = flipped_binary[:i] + [0] + flipped_binary[i+1:]

  return flipped_binary
 
#tests

#should print [1, 0, 1, 1, 1]
print(positive_to_negative([0, 1, 0, 0, 1]))
#should print [0, 0, 0, 0]
print(positive_to_negative([0, 0, 0, 0]))
#should print [1, 1, 1, 0]
print(positive_to_negative([0, 0, 1, 0]))
#should print [1, 1, 0, 1]
print(positive_to_negative([0, 0, 1, 1]))
#should print [1, 1, 0, 0]
print(positive_to_negative([0, 1, 0, 0]))
#should print [1, 1, 0, 0]
print(positive_to_negative([0, 1, 0, 0]))