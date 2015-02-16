n = input ("Enter n: ")
n = int(n)

m = input ("Enter m: ")
m = int(m)

if (n%10) > (m%10):
    print (n)
elif (n%10) < (m%10):
    print (m)
else:
    if n>m:
        print (n)
    else:
        print (m)
        
