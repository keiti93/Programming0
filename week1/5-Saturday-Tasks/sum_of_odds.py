n = input ("Enter n: ")
n = int(n)

sum = 0
a = 0

while a <= n:
    if a%2==1:
        sum = sum + a
    a=a+1
print (sum)
