def divisors(x):
    div = []
    divisor = 1
    while divisor != x:
        if x%divisor == 0:
            div = div + [divisor]
        divisor += 1
    return (div)

def main():
    n = input ("Enter n: ")
    n = int(n)

    print (divisors(n))

if __name__ == "__main__":
    main()
