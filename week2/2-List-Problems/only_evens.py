n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    count += 1
    
    if number%2==0:
        numbers = numbers + [number]
    
print ("Count of evens:", len(numbers))
print ("Evens are:")
print (numbers)
