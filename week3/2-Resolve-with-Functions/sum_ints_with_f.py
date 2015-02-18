from divisors_with_f import divisors

def sum_ints(xs):
    total_sum = 0
    for digit in xs:
        total_sum += digit
    return total_sum

def sum_divisors (x):
    return sum_ints(divisors(x))

def main():
    n = input ("Enter n: ")
    n = int(n)

    print (sum_divisors(n))

if __name__ == "__main__":
    main()
