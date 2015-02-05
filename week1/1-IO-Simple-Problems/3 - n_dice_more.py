from random import randint
a = input ("Enter sides:")
dice1 = randint(1, int(a))
dice2 = randint(1, int(a))
dice3 = randint(1, int(a))
print ("First Roll:")
print (dice1)
print ("Second Roll:")
print (dice2)
print ("Third Roll:")
print (dice3)
sum = dice1+dice2+dice3
print ("Sum is:")
print (sum)
