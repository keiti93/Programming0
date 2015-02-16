from random import randint

score_maria = 1001
score_ivan = 1001

dice_throws_maria = 0
dice_throws_ivan = 0

sum_maria = 0
sum_ivan = 0

while (score_maria!=0)and (score_ivan != 0):
    if score_maria>0:
        while dice_throws_maria<=6:
            n = randint (1,6)
            dice_throws_maria = dice_throws_maria + 1
            sum_maria = sum_maria + n
        score_maria = score_maria - sum_maria
        sum_maria = 0
        dice_throws_maria = 0
        print ("Maria: ", score_maria)
    elif score_maria<0:
        while dice_throws_maria<=6:
            n = randint (1,6)
            dice_throws_maria = dice_throws_maria + 1
            sum_maria = sum_maria + n
        score_maria = score_maria + sum_maria
        sum_maria = 0
        dice_throws_maria = 0
        print ("Maria: ", score_maria)

        
    if score_ivan>0:
        while dice_throws_ivan<=6:
            n = randint (1,6)
            dice_throws_ivan = dice_throws_ivan + 1
            sum_ivan = sum_ivan + n
        score_ivan = score_ivan - sum_ivan
        sum_ivan = 0
        dice_throws_ivan = 0
        print ("Ivan: ", score_ivan)
        print ()
    elif score_ivan<0:
        while dice_throws_ivan<=6:
            n = randint (1,6)
            dice_throws_ivan = dice_throws_ivan + 1
            sum_ivan = sum_ivan + n
        score_ivan = score_ivan + sum_ivan
        sum_ivan = 0
        dice_throws_ivan = 0
        print ("Ivan: ", score_ivan)
        print ()

if score_maria == 0:
    print ("Maria wins!")
elif score_ivan == 0:
    print ("Ivan wins!")
    
# Ама много тромаво!!!! :D
