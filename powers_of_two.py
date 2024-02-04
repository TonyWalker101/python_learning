#codewars kata => https://www.codewars.com/kata/57a083a57cb1f31db7000028/python

def powers_of_two(n):
  answer = []

  for num in range(0,n+1):
    answer.append(2**n)
  
  return answer

#tests

#should print [1]
print(powers_of_two(0))
#should print [1,2]
print(powers_of_two(1))
#should print [1, 2, 4, 8, 16]
print(powers_of_two(4))