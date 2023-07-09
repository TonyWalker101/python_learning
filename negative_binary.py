#codewars kata => https://www.codewars.com/kata/5becace7063291bebf0001d5/python

def positive_to_negative(binary):
  flipped_binary = list(map(lambda x: 0 if x == 1 else 1, binary))
  results = []
  # print(binary)

  if flipped_binary[-1] == 0:
    flipped_binary = flipped_binary[:-1]
    flipped_binary.append(1)
    return flipped_binary
  
  # for i in range(len(flipped_binary)-1, 0):
  #   if flipped_binary(i) == 0:
  #     flipped_binary = flipped_binary[:i] + flipped_binary[i:]
  #     flipped_binary.insert(i, 1)


  

  # print(flipped_binary)
  # return

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