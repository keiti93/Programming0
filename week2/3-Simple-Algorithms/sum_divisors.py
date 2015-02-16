n = input ("Enter n: ")
n = int(n)

sum_divisors = 0
divisor = 1

while divisor != n:
    if n%divisor==0:
        sum_divisors += divisor
    divisor += 1
    
print (sum_divisors)
