# program to practice dictionaries

#initial data
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#list comprehension to combine both lists
letter_to_points = {letters:points for letters, points in zip(letters, points)}
# print(letter_to_points)

#adding blank values to letters_to_points dict
letter_to_points[" "] = 0
# print(letter_to_points)

#function for determining letter's points
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

#testing score_word function, should return 15
brownie_points = score_word("BROWNIE")
# print(brownie_points)

#scrabble players and the words they've played
player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"],
  "wordNerd": ["EARTH", "EYES", "MACHINE"],
  "LexiCon": ["ERASER", "BELLY", "HUSKY"],
  "ProfReader": ["ZAP", "COMA", "PERIOD"]
}

#calculating player_to_words score
player_to_points = {}

for words in player_to_words:
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[words] = player_points

#test, wordNerd should be up 1 point
# print(player_to_points)