n = input ("Enter n: ")
n = int(n)

numbers = []
sum = 0
count = 1

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    count += 1
    sum += number

print ("The sum is:", sum)
