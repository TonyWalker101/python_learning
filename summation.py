# program to find sum of numbers up to the given number

def summation(num):
  answer = 0
  while num >= 1:
    answer += num
    num -= 1
  return answer

#tests

#should return 1
print(summation(1))
#should return 36
print(summation(8))
#should return 253
print(summation(22))
#should return 5050
print(summation(100))