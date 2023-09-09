#codewars kata => https://www.codewars.com/kata/5663f5305102699bad000056/python

def mxdiflg(a1, a2):
  mx = -1
  for x in a1:
    for y in a2:
      diff = abs(len(x) - len(y))
      if (diff > mx):
        mx = diff

  return mx

#tests

#should print 13
s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2))
#should print 10
s1 = ["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"]
s2 = ["bbbaaayddqbbrrrv"]
print(mxdiflg(s1, s2))
#should print -1
s2 = []
s1 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2)) 