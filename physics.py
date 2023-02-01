# program to practice functions

# fahrenheit to celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celcius = f_to_c(100)
print(f100_in_celcius)

#celsius to fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * 9/5 + 32
  return f_temp

