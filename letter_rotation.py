#kata to move first letter in word around itself

def rotate(str_):
  #your code here
  answer = []
  first_letter = str_[0]
  current_word = str_
  start_index = 0
  end_index = -1
  for i in range(len(str_)):
      H_index = current_word.index(first_letter)
      new_word = str_.replace(first_letter,current_word[H_index+1]
      
      new_word[last_index] = str[first_index]
      answer.append(new_word)
      index++
  return answer

#tests

#should return ["231", "312", "123"]
print(rotate("123"))