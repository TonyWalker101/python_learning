#codewars kata => https://www.codewars.com/kata/53697be005f803751e0015aa

#refactored solution

cipher = ("aeiou", "12345")

def encode(st):
  return st.translate(str.maketrans(cipher[0], cipher[1]))
    
def decode(st):
  return st.translate(str.maketrans(cipher[1], cipher[0]))

#tests

#should print 'h2ll4'
print(encode('hello'))
#should print 'H4w 1r2 y45 t4d1y?'
print(encode('How are you today?'))
#should print 'Th3s 3s 1n 2nc4d3ng t2st.'
print(encode('This is an encoding test.'))
#should print 'hello'
print(decode('h2ll4'))