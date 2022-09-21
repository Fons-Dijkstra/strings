# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
speler1 = 'Gullit'
speler2 = 'Van Basten'
goal_0 = "32"
goal_1 = "54"
scorers = speler1 + " " + goal_0, speler2 + " " + goal_1
print(scorers)
report = (((speler1) + " " + "scored in the" + " " + f'{goal_0}nd minute\n') + ((speler2) + " " + "scored in the" + " " + f'{goal_1}th minute'))
print(report)
player = 'Jan Wouters'
first_name = (player[0:3])
print(first_name)
x = player.find('Jan')
print(x)
y = player.find('Wouters')
print(y)
last_name_len = (player[4:11])
print(last_name_len)
z = len(last_name_len)
print(z)
first_letter = (player[0] + ".")
last_name = (player[4:11])
print(first_letter + " " + last_name)
ex = '!'
first_name_len = len(first_name)
chant = ((first_name + ex + " ") * first_name_len) [:-1]
print(chant)
print(chant != " ")