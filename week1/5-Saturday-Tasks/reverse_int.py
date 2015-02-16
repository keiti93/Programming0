n = input ("Enter n: ")
n = int(n)

m = 0

while n!=0:
    a = n%10
    m = m * 10 + a
    n = n//10

print (m)
