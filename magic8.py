#magic 8 ball program that responds to user questions

import random
import sys

# setup
name = input("Hello! What is your name? ")

question = input("Ask me a Yes or No question: ")

answer = ""

# if missing user input
if name == "" or question == "":
  print("I need a name and question in order to predict the future!")
  sys.exit()

# answer logic
random_number = random.randint(1,9)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  answer = "Error"

#final output

print(name," asks: ", question)
print("Magic 8-Ball's answer: ", answer)