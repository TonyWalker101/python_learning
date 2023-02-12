# tarot generating program

#for random num generation
import numpy as np

tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}
spread = {}

#available cards left in the tarot deck
cards_left = list(tarot.keys())

#for each choice, numpy will select a random num from the available cards in tarot
spread["past"] = tarot.pop(np.random.choice(cards_left))
spread["present"] = tarot.pop(np.random.choice(cards_left))
spread["future"] = tarot.pop(np.random.choice(cards_left))

# final results
for card,value in spread.items():
  print(f'Your {card} is the {value} card.')
