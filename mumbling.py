#kata to emulate mumbling via string manipulation

def accum(word):
  length = len(word)
  answer = ""
  for i in range(length):
    mumble_to_add = word[i] * (i + 1)
    answer += mumble_to_add.title()
    if i < length-1:
      answer += "-"

  return answer

#tests

#should print "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
print(accum("ZpglnRxqenU"))
#should print "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb"
print(accum("NyffsGeyylB"))
#should print "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu"
print(accum("MjtkuBovqrU"))
#should print "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm"
print(accum("EvidjUnokmM"))
#should print "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc"
print(accum("HbideVbxncC"))