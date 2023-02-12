#tarot generating program using Numpy module

#for random num generation
import numpy as np

#starting variables
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}
your_future = {"past": "", "present": "", "future": ""}

for prediction in your_future.keys():
#available cards left in the tarot deck
  cards_left = list(tarot.keys())
#for each prediction, numpy will select a random num from the available cards in tarot
  your_future[prediction] = tarot.pop(np.random.choice(cards_left))

#final results
for key,value in your_future.items():
  print(f'Your {key} is the {value} card.')