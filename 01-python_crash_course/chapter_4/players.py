players = ['charles', 'martina', 'michael', 'florence', 'eli']
#Slice:
# ~ print(players[0:3]) 
# ~ print(players[1:4])
# ~ print(players[:4]) #empieza en el índice 0
# ~ print(players[2:]) #termina al final
# ~ print(players[-3:]) #ultimos tres
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
