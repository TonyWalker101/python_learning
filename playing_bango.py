#codewars kata => https://www.codewars.com/kata/53af2b8861023f1d88000832/python

def are_you_playing_banjo(name):
    # Implement me!
    return name + " plays banjo" if name.lower().startswith("r") else name + " does not play banjo"

#tests

#should print "martin does not play banjo"
print(are_you_playing_banjo("martin"))
#should print "Rikke plays banjo"
print(are_you_playing_banjo("Rikke"))
#should print "bravo does not play banjo"
print(are_you_playing_banjo("bravo"))
#should print "rolf plays banjo"
print(are_you_playing_banjo("rolf"))
    