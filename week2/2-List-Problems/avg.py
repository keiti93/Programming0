n = input ("Enter n: ")
n = int(n)

numbers = []
count = 1
sum = 0

while count <= n:
    number = input()
    number = int(number)
    count += 1
    numbers = numbers + [number]
    
for number in numbers:
    sum += number
    
print ("Avg is:", sum/ len(numbers) )
