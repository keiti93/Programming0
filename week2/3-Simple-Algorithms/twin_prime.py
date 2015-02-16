# без функция

p = input ("Enter p: ")
p = int(p)

start = 2
is_prime = True

if p == 1:
    is_prime = False

while start < p:
    if p % start == 0:
        is_prime = False
        break
    start = start + 1

a = p+2
b = p-2

start_a = 2
a_prime = True

if a == 1:
    is_prime = False

while start_a < a:
    if a % start_a == 0:
        a_prime = False
        break
    start_a = start_a + 1

start_b = 2
b_prime = True

if b == 1:
    b_prime = False

while start_b < b:
    if b % start_b == 0:
        b_prime = False
        break
    start_b = start_b + 1

if is_prime and a_prime:
    if b_prime:
        print ("Twin primes with",p, ":")
        print (p, a)
        print (b, p)
    else:
        print ("Twin primes with",p, ":")
        print (p, a)
elif is_prime and b_prime:
    print ("Twin primes with",p, ":")
    print (b, p)
elif is_prime and not a_prime:
    if not b_prime:
        print (p, "is prime but:")
        print (b, "is not")
        print (a, "is not")
else:
    print (p, "is not a prime!")
