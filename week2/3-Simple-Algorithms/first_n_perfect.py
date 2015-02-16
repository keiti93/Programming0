n = input ("Enter n: ")
n = int(n)


sum_divisors = 0
number = 5
divisor = 1
count = 0

while True:
    number += 1
    
    while divisor != number:
        
        if number%divisor==0:
            sum_divisors += divisor
        divisor += 1
        
    if sum_divisors == number:
        print (number)
        count += 1
            
        if count == n:
            break
    else:
        sum_divisors = 0
        divisor = 1
