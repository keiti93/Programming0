def reverse_int(x):

    number = 0
    
    while x !=0:
        a = x%10
        number = number*10 + a
        x = x//10
        
    return number

def sum_digits(x):

    total_sum = 0
    
    while x!=0:
        a = x%10
        total_sum += a
        x = x//10
        
    return total_sum

def product_digits(x):

    product = 1
    
    while x!=0:
        a = x%10
        product = product*a
        x = x//10
        
    return product

n = input("Enter number: ")
n = int(n)

print ("The number reversed:", reverse_int(n))
print ("The sum of the digits:", sum_digits(n))
print ("The product of the digits:", product_digits(n))
