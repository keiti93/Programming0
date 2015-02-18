from divisors_with_f import divisors
from sum_ints_with_f import sum_ints, sum_divisors
from is_perfect_with_f import is_perfect

def main():
    n = input("Enter n: ")
    n = int(n)

    counter = 0 
    x = 6
    
    while True:
        if is_perfect(x) == True:
            print (x)
            counter += 1
            if counter == n:
                break
        x += 1

if __name__ == "__main__":
    main()
