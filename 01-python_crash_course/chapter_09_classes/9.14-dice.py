from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_die(self):
        """
        Prints a random number between 1
        and the number of sides of the die
        """
        number = randint(1, self.sides) 
        print(number)



die = Die()
times = 0
print("6 sided die: ")
while times < 10:
    die.roll_die()
    times += 1

die = Die(10)
times = 0
print("\n10 sided die: ")
while times < 10:
    die.roll_die()
    times += 1

die = Die(20)
times = 0
print("\n20 sided die: ")
while times < 10:
    die.roll_die()
    times += 1
