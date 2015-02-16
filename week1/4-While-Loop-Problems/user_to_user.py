a = input ("enter a: ")
b = input ("enter b: ")
a = int(a)
b = int(b)

if a<b:
    while a <= b:
        print (a)
        a = a+1
else:
    while b <= a:
        print (b)
        b = b+1
        
