n = input ("Enter n: ")
n = int(n)

sum_divisors = 0
divisor = 1

while divisor != n:
    if n%divisor==0:
        sum_divisors += divisor
    divisor += 1
    
if sum_divisors == n:
    print ("Yes, the number", n,  "is perfect!")
else:
    print ("No, the number", n, "is not perfect, because the sum of its divisors is", sum_divisors)
