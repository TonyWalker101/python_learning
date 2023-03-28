# greeting card generating program to practice creating custom context managers using contextlib module and context manager class

from contextlib import contextmanager

@contextmanager
def generic(sender_name, card_type, receiver_name):
  if "birthday" in card_type:
    generic_card = open("happy_bday.txt","r")
  else:
    generic_card = open("thankyou_card.txt", "r")

  personalized_card = open(f"{sender_name}_generic.txt", "w")

  try:
    personalized_card.write(f"Dear {receiver_name.title()}\n")
    personalized_card.write(generic_card.read())
    personalized_card.write(f"\nSincerely, {sender_name.title()}")
    yield personalized_card
  finally:
    generic_card.close()
    personalized_card.close()
    
sender_name = "Mwenda"
with generic(sender_name, "thank you","Amanda") as card:
    print("Card Generated!")
  
with open(f"{sender_name}_generic.txt", "r") as first_card:
    print(first_card.read())

class Personalized:
  def __init__(self, sender, receiver, message):
    self.sender = sender
    self.receiver = receiver
    self.msg = message
    self.file = open(f"{self.sender}_personalized.txt", "w")
  
  def __enter__(self):
    self.file.write(f"Dear {self.receiver}\n")
    self.file.write(f"{self.msg}")
  
  def __exit__(self, exc_type, exc_value, traceback):
    self.file.write(f"\nSincerely, {self.sender}")
    self.file.close()

with Personalized("John","Michael","I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.") as new_card:
  print("Personalized Card Generated!")

with generic("Josiah", "birthday", "Remy") as bday_card:
  print("Bday card generated for Remy!")

with Personalized("Josiah", "Esther", "Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!") as personalized_card:
  print("Personalized card created for Esther!")
  