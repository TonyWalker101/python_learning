# 9. Palindrome Number

class Solution:
  def isPalindrome(self, x):
      if x < 0:
          return False

      div = 1
      while x >= 10 * div:
          div *= 10
      
      while x != 0: 
          left = x // div
          right = x % 10

          if left != right:
              return False
          
          x = (x % div) // 10
          div /= 100

      return True
