from random import randint
sides = input ("Enter sides: ")
name1 = input ("Enter player1: ")
name2 = input ("Enter player2: ")
number1 = randint (1, int(sides))
number2 = randint (1, int(sides))
print (name1 + " rolls ", number1)
print (name2 + " rolls ", number2)
if number1>number2:
    print (name1 + " wins!")
elif number2>number1:
    print (name2 + " wins!")
else:
    print ("The numbers are equal.")
