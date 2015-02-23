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

def fib_number(numbers):
    number = 0
    for num in numbers:
        if num>9 and num<100:
            number = number*100 + num
        elif num>99 and num<1000:
            number = number*1000 + num
        elif num>999 and num<10000:
            number = number*10000 + num
        elif num>9999 and num<100000:
            number = number*100000 + num
        else:
            number = number*10 + num
    return number

n = input("Enter n: ")
n = int(n)

print (fib(n))
print (fib_number(fib(n)))
