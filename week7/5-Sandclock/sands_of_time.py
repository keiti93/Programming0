n = input("Enter n: ")
n = int(n)

number_of_stars = n
star = "*"
number_of_dots = 0
dot = "."

while number_of_stars >= 1:
    print(number_of_dots*dot + star*number_of_stars + number_of_dots*dot)
    number_of_stars -= 2
    number_of_dots += 1
    if number_of_stars == 1:
        break
        
while number_of_stars < n + 1:
    print(number_of_dots*dot + star*number_of_stars + number_of_dots*dot)
    number_of_stars += 2
    number_of_dots -= 1
    if number_of_stars == n+1:
        break
