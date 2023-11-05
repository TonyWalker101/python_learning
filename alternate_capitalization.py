#codewars kata => https://www.codewars.com/kata/59cfc000aeb2844d16000075/python

def capitalize(s):
  string_1 = ""
  string_2 = ""

  for x in range(len(s)):
    if x % 2 != 0:
      string_1 += s[x].upper()
      string_2 += s[x].lower()

    if x % 2 == 0:
      string_1 += s[x].lower()
      string_2 += s[x].upper()
  
  return [string_2, string_1]

#tests

#should print ['AbCdEf', 'aBcDeF']
print(capitalize("abcdef"))
#should print ['CoDeWaRs', 'cOdEwArS']
print(capitalize("codewars"))
#should print ['AbRaCaDaBrA', 'aBrAcAdAbRa']
print(capitalize("abracadabra"))
#should print ['CoDeWaRrIoRs', 'cOdEwArRiOrS']
print(capitalize("codewarriors"))