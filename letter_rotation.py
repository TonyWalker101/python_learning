#kata to move first letter in word around itself

def rotate(str_):
  return [str_[i+1:] + str_[:i+1] for i in range(len(str_))]

#tests

#should return ["231", "312", "123"]
print(rotate("123"))
#should return ["elloH", "lloHe", "loHel", "oHell", "Hello"]
print(rotate("Hello"))