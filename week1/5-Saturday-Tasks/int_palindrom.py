n = input ("Enter n: ")
n = int(n)

m = n
new = 0

while n!=0:
    a = n%10
    new = new*10 + a
    n = n//10

if new == m:
    print ("The number is a palindrom")
else:
    print ("The number is not a palindrom")
