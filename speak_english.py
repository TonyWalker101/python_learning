#codewars kata => https://www.codewars.com/kata/58dbdccee5ee8fa2f9000058/python

def sp_eng(sentence): 
  return "english" in sentence.lower()

#tests

#should print True
print(sp_eng("english"))
#should print False
print(sp_eng("egnlish"))
#should print False
print(sp_eng("1234egn lis;h"))
#should print True
print(sp_eng("1234english ;k"))
#should print True
print(sp_eng("English"))
#should print True
print(sp_eng("eNgliSh"))
#should print True
print(sp_eng("1234#$%%eNglish ;k9"))
#should print False
print(sp_eng("EGNlihs"))
#should print False
print(sp_eng("1234englihs**"))