# program to find sum of numbers up to the given number

def summation(num):
  start = 1
  answer = 0
  while start < num:
    answer += start
    start += 1
  return answer

#tests

#should return 1
print(summation(1))
#should return 36
print(summation(8))
#should return 256
print(summation(22))