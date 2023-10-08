#codewars kata => https://www.codewars.com/kata/57158fb92ad763bb180004e7/python

def rain_amount(mm):
  if (mm < 40):
    return "You need to give your plant {}mm of water".format(40-mm)
  else:
    return "Your plant has had more than enough water for today!"
  
#tests

#should print "Your plant has had more than enough water for today!"
print(rain_amount(100))
#should print "Your plant has had more than enough water for today!"
print(rain_amount(40))
#should print "You need to give your plant 1mm of water"
print(rain_amount(39))
#should print "You need to give your plant 35mm of water"
print(rain_amount(5))
#should print "You need to give your plant 40mm of water"
print(rain_amount(0))