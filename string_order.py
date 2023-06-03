#codewars kata => https://www.codewars.com/kata/55c45be3b2079eccff00010f/python

def order(sentence):
  if not sentence:
    return ""
  
  def get_digit(word):
    for char in word:
      if char.isdigit():
        return int(char)
  
  sentence_list = sentence.split(" ")
  index = len(sentence_list) - 1
  sorted = False

  while not sorted:
    sorted = True
    for i in range(index):
      if get_digit(sentence_list[i]) > get_digit(sentence_list[i+1]):
        sentence_list[i], sentence_list[i+1] = sentence_list[i+1], sentence_list[i]
        sorted = False
    index -= 1
  
  return " ".join(sentence_list)


#should print "Thi1s is2 3a T4est"
print(order("is2 Thi1s T4est 3a"))
#should print "Fo1r the2 g3ood 4of th5e pe6ople"
print(order("4of Fo1r pe6ople g3ood th5e the2"))
#should print ""
print(order(""))