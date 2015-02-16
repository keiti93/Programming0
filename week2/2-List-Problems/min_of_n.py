n = input ("Enter n: ")
n = int(n)

numbers = []
count = 1

while count <= n:
    number = input()
    number = int(number)
    count += 1
    numbers = numbers + [number]
    
a = numbers[0]

for number in numbers:
    if number<a:
        a = number

print ("Min is:", a)
