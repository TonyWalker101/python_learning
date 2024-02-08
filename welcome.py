#codewars kata => https://www.codewars.com/kata/577ff15ad648a14b780000e7/python

def greet(language):
  languages_lst = [ ("english", "Welcome")
, ("czech", "Vitejte")
, ("danish", "Velkomst")
, ("dutch", "Welkom")
, ("estonian", "Tere tulemast")
, ("finnish", "Tervetuloa")
, ("flemish", "Welgekomen")
, ("french", "Bienvenue")
, ("german", "Willkommen")
, ("irish", "Failte")
, ("italian", "Benvenuto")
, ("latvian", "Gaidits")
, ("lithuanian", "Laukiamas")
, ("polish", "Witamy")
, ("spanish", "Bienvenido")
, ("swedish", "Valkommen")
, ("welsh", "Croeso")]
  
  for lang in languages_lst:
    if lang[0] == language:
      return lang[1]
  
  return "Welcome"

#tests

#should print Welcome
print(greet('english'))
#should print Welkom
print(greet('dutch'))
#should print Welcome
print(greet('IP_ADDRESS_INVALID'))
#should print Welcome
print(greet(''))
#should print Welcome
print(greet(2))