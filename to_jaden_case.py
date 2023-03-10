#program to title case every word in a sentence, like Jaden Smith on Twitter

#initial solution
# def to_jaden_case(string):

#   title_string = string.split()
#   for i in range(len(title_string)):
#     title_string[i] = title_string[i].capitalize()
  
#   return  " ".join(title_string).strip()

#refactor #1
def to_jaden_case(string):
  return  " ".join(word.capitalize() for word in string.split())

#refactor #2 using string built-in module
# import string

# def to_jaden_case(sentence):
#   return string.capwords(sentence)


#tests
#should equal "How Can Mirrors Be Real If Our Eyes Aren't Real"
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
