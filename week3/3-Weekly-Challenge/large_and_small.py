n = input ("Enter n: ")


numbers = []
numbers += n
a = ''
b =''
numbers.sort()
for number in numbers:
    a = a + str(number)
print ("Smallest:", int (a))

numbers.sort(reverse=True)
for number in numbers:
    b = b + str(number)
print ("Largest:", b)
