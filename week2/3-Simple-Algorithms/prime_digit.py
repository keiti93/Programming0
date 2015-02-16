n = input("Enter n: ")
n = int(n)

is_prime = False

while n != 0:
    a = n%10
    if a in [1,2,3,5,7]:
        is_prime = True
    n = n//10

if is_prime:
    print("Yes")
else:
    print("No")
