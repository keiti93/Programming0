a = input ("Enter a: ")
b = input ("Enter b: ")
a = int(a)
b = int(b)
if a>b:
    print ("a (%s) is bigger than b (%s)" % (a,b))
elif b>a:
    print ("b (%s) is bigger than a (%s)" % (b,a))
else:
    print ("a (%s) is equal to b (%s)" % (a,b))
