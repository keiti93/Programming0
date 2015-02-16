n = input ("Enter number: ")
n = int(n)

digits = []

while n != 0:
    digits = [n%10] + digits
    n = n//10

print ("List of digits is:", digits)

number = 0

for digit in digits:
    number = number*10 + digit

print ("Number is:", number)
