#program to join words from a list together

def smash(words):
  return " ".join(words)

#tests

#should print "hello world"
print(smash(["hello", "world"]))

#should print "hello amazing world"
print(smash(["hello", "amazing", "world"]))

#should print "this is a really long sentence"
print(smash(["this", "is", "a", "really", "long", "sentence"]))
