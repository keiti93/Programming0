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
        
        if num>9:
            numbers_new = []
            y = 0
            original = num
            
            while num != 0:
                numbers_new = numbers_new + [num%10]
                num = num//10
            new_list = numbers_new[::-1]

            new_number = 0
            
            for num1 in new_list:
                new_number = new_number*10 + num1

            number = number* (10**len(numbers_new)) + new_number
            num = original
        else:
            number = number*10 + num
            
    return number

n = input("Enter n: ")
n = int(n)

print (fib(n))
print (fib_number(fib(n)))
