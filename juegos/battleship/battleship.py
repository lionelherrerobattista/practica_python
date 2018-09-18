from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)

#Función que imprime el tablero
def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

#Funciones que generan un barco en fila y columna aleatoria
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#Muestra la columna y la fila del barco
print (ship_row)
print (ship_col)


#Juego de 4 intentos
turn = 0
for turn in range(4):
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sunk my battleship!")
    break
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print ("Oops, that's not even in the ocean.")
    elif(board[guess_row][guess_col] == "X"):
      print ("You guessed that one already.")
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
      if turn == 3:
        print ("Game Over")
    #Imprime el turno y agrega 1
    turn += 1
    print ("Turn: " + str(turn))
    print_board(board)
