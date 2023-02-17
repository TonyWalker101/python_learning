# program to title case every word in a sentence, like Jaden Smith on Twitter

def to_jaden_case(string):
# answer = ""
  title_string = string.split()
  print("title_string #1", title_string)
  for i in range(len(title_string)):
    title_string[i] = title_string[i].title()
  
  print("title_string #2", title_string)
  answer = " ".join(title_string)
  answer.strip()
  return answer

# tests

#should equal "How Can Mirrors Be Real If Our Eyes Aren't Real"

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
