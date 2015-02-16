a = input ("enter a: ")
b = input ("enter b: ")
a = int(a)
b = int(b)

while a != b+1:
    if a%2==0:
        print (a, " - even")
    else:
        print (a, " - odd")
    a = a+1
