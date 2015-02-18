def is_prime(number):
    start = 2
    is_pr = True

    if number == 1:
        is_pr = False

    while start < number:
        if number % start == 0:
            is_pr = False
            break
        start = start + 1    
    return is_pr

def to_digits(n):
    digits = []
    while n != 0:
        digits = [n%10] + digits
        n = n//10
    return digits

def main():
    n = input("Enter n: ")
    n = int(n)

    count = 0
    for digit in to_digits(n):
        if is_prime(digit) == True:
            print ("Yes")
            count += 1
            break
    if count == 0:
        print ("No")

if __name__ == "__main__":
    main()
