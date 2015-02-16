a = input ("Въведи резултат: ")
a = int(a)


if (a>=0) and (a<=100):
    if a <= 50:
        print ("Слаб 2")
    elif 51 <= a <= 60:
        print ("Среден 3")
    elif 61 <= a <= 70:
        print ("Добър 4") 
    elif 71 <= a <= 80:
        print ("Много добър 5")
    elif 81 <= a < 100:
        print ("Отличен 6")
    else:
        print ("Много Отличен 7")
else:
    print ("Грешен резултат")
