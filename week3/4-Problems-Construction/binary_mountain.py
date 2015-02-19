n = input ("Enter number: ")
n = int(n)

original = n

bin_list = []
while n != 0:
    a = n%2
    bin_list = [a] + bin_list
    n = n//10


def take(n, items):
    result = []
    start = 0
    while start <n and start < len(items):
        item = items[start]
        result = result + [item]
        start += 1
    return result

def drop(n, items):
    result = []
    start = n
    while start < len(items):
        item = items[start]
        result = result + [item]
        start += 1
    return result

def chislo (x):
    number = 0
    for digit in x:
        number = number*10 + digit
    return number

print ("In binary,", original, "is:", chislo(bin_list))

print ("The triangle is:")

counter = 1
while len(bin_list) != 0:
    print (take(counter, bin_list))
    bin_list = drop(counter, bin_list)
    counter += 1
    if counter > len(bin_list):
        break
