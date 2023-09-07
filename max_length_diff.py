#codewars kata => https://www.codewars.com/kata/5663f5305102699bad000056/python

def mxdiflg(a1, a2):
  if not a1 and not a2:
    return -1
  
  return max(abs(len(a1) - len(a2)))


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