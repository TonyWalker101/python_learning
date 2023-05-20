#codewars kata (converted to python) => https://www.codewars.com/kata/620e839683ba7e003ea49757

def calc_shape(x):
  width = x[0]
  length = x[1]

  return [width*length if width == length else 2*(width+length)]


#area calculation tests

#should print ([25]
print(calc_shape([5, 5]))
#should print [49]
print(calc_shape([7, 7]))

#perimeter calculation tests

#should print [18]
print(calc_shape([4, 5]))
#should print [24]
print(calc_shape([7, 5]))