N = input ("Enter N: ")
M = input ("Enter M: ")
N = int(N)
M = int(M)

sum = 0
if N<M:
    n=N
    while n<=M:
       sum = n%10 + sum
       print ("Sum of digits of ", n, " = ", sum)
       n = n+1
       sum = 0
       a = n//10
       if a!=0:
           sum = sum + a
       else:
           sum = 0

elif N>M:
    n=M
    while n<=N:
       sum = n%10 + sum
       print ("Sum of digits of ", n, " = ", sum)
       n = n+1
       sum = 0
       a = n//10
       if a!=0:
           sum = sum + a
       else:
           sum = 0
else:
    print ("N = M")
