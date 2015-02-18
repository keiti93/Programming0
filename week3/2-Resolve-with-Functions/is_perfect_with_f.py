from divisors_with_f import divisors
from sum_ints_with_f import sum_ints, sum_divisors

def is_perfect(x):
    if x == sum_divisors(x):
        return True
    else:
        return False

def main():
    n = input ("Enter n: ")
    n = int(n)

    if is_perfect(n) == True:
        print ("The number is perfect!")
    else:
        print ("The number is not perfect!")
    
if __name__ == "__main__":
    main()
