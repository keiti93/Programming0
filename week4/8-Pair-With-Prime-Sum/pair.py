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

def prime_pair(numbers):
    for index_x in range(0, len(numbers)):
        for index_y in range (index_x, len(numbers)):
            x = numbers[index_x]
            y = numbers[index_y]
            a = x + y
            if is_prime(a)== True:
                return True
    return False

