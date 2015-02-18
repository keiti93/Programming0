from prime_digit_with_f import is_prime

def main():
    n = input("Enter n: ")
    n = int(n)

    p1 = n+2
    p2 = n-2

    if is_prime(n) == True and is_prime(p1) == True and is_prime(p2) == True:
        print ("Twin primes with", n, ":")
        print (p2, n)
        print (n, p1)
        
    elif is_prime(n) == True and is_prime(p1):
        print ("Twin prime with", n, ":")
        print (n, p1)
        
    elif is_prime(n) == True and is_prime(p2):
        print ("Twin prime with", n, ":")
        print (p2, n)
        
    elif is_prime(n) == True and is_prime(p1) == False and is_prime(p2) == False:
        print (n, "is prime but:")
        print (p2, "is not.")
        print (p1, "is not.")
        
    else:
        print (n, "is not a prime.")

if __name__ == "__main__":
    main()
