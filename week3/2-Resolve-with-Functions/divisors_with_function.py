def divisors(n):
    divisors_list = []
    divisor = 1
    while divisor != n:
        if n%divisor==0:
            divisors_list = divisors_list + [divisor]
        divisor += 1
    return (divisors_list)


n = input ("Enter n: ")
n = int(n)

print (divisors(n))
