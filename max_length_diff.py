#codewars kata => https://www.codewars.com/kata/5663f5305102699bad000056/python

def mxdiflg(a1, a2):
  if a1 and a2:
    return max(abs(len(x) - len(y)) for x in a1 for y in a2)

  return -1


#tests

#should print 13
s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2))
#should print 10
s1 = ["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"]
s2 = ["bbbaaayddqbbrrrv"]
print(mxdiflg(s1, s2), 10)
#should print -1
s2 = []
s1 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2), -1) 