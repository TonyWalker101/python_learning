#codewars kata => https://www.codewars.com/kata/5bd00c99dbc73908bb00057a

import string

def alpha_seq(s):
  results = ""
  for letter in sorted(s):
    results += letter * (string.ascii_letters.index(letter) + 1) + ","
  return results[:-1]

  # return ",".join([letter * (string.ascii_letters.index(letter) + 1) for letter in sorted(s)])

#tests


print(alpha_seq("a"))
#should print "A,Bb,Ccc,Ffffff,Ffffff"
print(alpha_seq("BfcFA"))
#should print "Eeeee,Ggggggg,Llllllllllll,Nnnnnnnnnnnnnn,Nnnnnnnnnnnnnn,Pppppppppppppppp,Qqqqqqqqqqqqqqqqq,Rrrrrrrrrrrrrrrrrr,Uuuuuuuuuuuuuuuuuuuuu,Xxxxxxxxxxxxxxxxxxxxxxxx,Zzzzzzzzzzzzzzzzzzzzzzzzzz"
print(alpha_seq("ZpglnRxqenU"))
#should print "Bb,Eeeee,Ffffff,Ffffff,Ggggggg,Llllllllllll,Nnnnnnnnnnnnnn,Sssssssssssssssssss,Yyyyyyyyyyyyyyyyyyyyyyyyy,Yyyyyyyyyyyyyyyyyyyyyyyyy,Yyyyyyyyyyyyyyyyyyyyyyyyy"
print(alpha_seq("NyffsGeyylB"))
#should print "Bb,Jjjjjjjjjj,Kkkkkkkkkkk,Mmmmmmmmmmmmm,Ooooooooooooooo,Qqqqqqqqqqqqqqqqq,Rrrrrrrrrrrrrrrrrr,Tttttttttttttttttttt,Uuuuuuuuuuuuuuuuuuuuu,Uuuuuuuuuuuuuuuuuuuuu,Vvvvvvvvvvvvvvvvvvvvvv"
print(alpha_seq("MjtkuBovqrU"))
#should print "Dddd,Eeeee,Iiiiiiiii,Jjjjjjjjjj,Kkkkkkkkkkk,Mmmmmmmmmmmmm,Mmmmmmmmmmmmm,Nnnnnnnnnnnnnn,Ooooooooooooooo,Uuuuuuuuuuuuuuuuuuuuu,Vvvvvvvvvvvvvvvvvvvvvv"
print(alpha_seq("EvidjUnokmM"))
#should print "Bb,Bb,Ccc,Ccc,Dddd,Eeeee,Hhhhhhhh,Iiiiiiiii,Nnnnnnnnnnnnnn,Vvvvvvvvvvvvvvvvvvvvvv,Xxxxxxxxxxxxxxxxxxxxxxxx"
print(alpha_seq("HbideVbxncC"))