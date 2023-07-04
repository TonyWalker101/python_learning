#codewars kata => https://www.codewars.com/kata/555eded1ad94b00403000071/python

def series_sum(n):
  return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

#tests

#should print "1.00"
print(series_sum(1))
#should print "1.25"
print(series_sum(2))
#should print "1.39"
print(series_sum(3))