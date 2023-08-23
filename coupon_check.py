#codewars kata => https://www.codewars.com/kata/539de388a540db7fec000642/python

import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
  if entered_code is correct_code:
      return(datetime.datetime.strptime(current_date,'%B %d, %Y') <= datetime.datetime.strptime(expiration_date,'%B %d, %Y'))
  return False

#should print True
print(check_coupon('123','123','September 5, 2014','October 1, 2014'))
#should print False
print(check_coupon('123a','123','September 5, 2014','October 1, 2014'))