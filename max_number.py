# program from determining max number

def max_num(num1, num2, num3):
  parameters = [num1, num2, num3]
  answer = max(parameters)

  if (parameters.count(answer) != 1):
    return "It's a tie!"
  else :
    return answer

# tests  

# should print 10
print(max_num(-10, 0, 10))
# should print 5
print(max_num(-10, 5, -30))
# should print -5
print(max_num(-5, -10, -10))
# should print "It's a tie!"
print(max_num(2, 3, 3))