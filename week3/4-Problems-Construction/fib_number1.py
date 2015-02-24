def fib(x):
    fib_list = [1, 1]
    if x == 1:
        fib_list = [1]
    elif x == 2:
        fib_list = [1, 1]
    else:
        count = 1
        while count != x - 1:
            fib_list = fib_list + [fib_list[count-1]+ fib_list[count]]
            count += 1
    return fib_list

def counter(x):
    result = 0
    while x != 0:
        result += 1
        x = x//10

    return result


def fib_number(numbers):
    number = 0
    
    for num in numbers:
        
        if num>9:
            zeros = 10**counter(num)
            number = number*zeros + num
        else:
            number = number*10 + num
            
    return number

n = input("Enter n: ")
n = int(n)

print (fib(n))
print (fib_number(fib(n)))
