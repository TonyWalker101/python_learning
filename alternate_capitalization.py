#codewars kata => https://www.codewars.com/kata/59cfc000aeb2844d16000075/python

def capitalize(s):
  results = []

  results.append("".join(map(lambda x: x.upper() if s.index(x) % 2 == 0 else x,s.lower())))

  results.append("".join(map(lambda x: x.upper() if s.index(x) % 2 != 0 else x,s.lower())))

  return results
#tests

#should print ['AbCdEf', 'aBcDeF']
print(capitalize("abcdef"))
#should print ['CoDeWaRs', 'cOdEwArS']
print(capitalize("codewars"))
#should print ['AbRaCaDaBrA', 'aBrAcAdAbRa']
print(capitalize("abracadabra"))
#should print ['CoDeWaRrIoRs', 'cOdEwArRiOrS']
print(capitalize("codewarriors"))