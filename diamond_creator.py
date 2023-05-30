#codewars kata => https://www.codewars.com/kata/5503013e34137eeeaa001648/python

def diamond(n):
  if n > 0 and n % 2 == 1:
      diamond = ""
      for i in range(n):
          diamond += " " * abs((n/2) - i)
          diamond += "*" * (n - abs((n-1) - 2 * i))
          diamond += "\n"
      return diamond
  else:
      return None
  
#tests

diamond(5)

