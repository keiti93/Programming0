n = input ("Enter n: ")
n = int(n)

divisors = []
divisor = 1

while divisor != n:
    if n%divisor==0:
        divisors = divisors + [divisor]
    divisor += 1

print (divisors)
