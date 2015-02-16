n = input ("Enter n: ")
n = int(n)

a = 2
if n==1:
    print ("The number is not prime!")
else:
    while a != n:
        if n%a==0:
            print ("The numbe is not prime!")
            break
        else:
            a = a+1

    if a==n:
        print ("The number is prime.")
