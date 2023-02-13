# program to practice dictionaries

#initial data
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#list comprehension to combine both lists
letter_to_points = {letters:points for letters, points in zip(letters, points)}
# print(letter_to_points)

#adding blank values to letters_to_points dict
letter_to_points[" "] = 0
print(letter_to_points)