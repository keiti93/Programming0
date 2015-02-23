first_row = []
count1 = 1
print ("Въведи първи ред на квадрата: ")

while count1 <= 3:
    row1 = input()
    row1 = int(row1)
    count1 += 1
    first_row = first_row + [row1]


second_row = []
count2 = 1
print ("Въведи втори ред на квадрата: ")

while count2 <= 3:
    row2 = input()
    row2 = int(row2)
    count2 += 1
    second_row = second_row + [row2]

third_row = []
count3 = 1
print ("Въведи трети ред на квадрата: ")

while count3 <= 3:
    row3 = input()
    row3 = int(row3)
    count3 += 1
    third_row = third_row + [row3]

magic_square = [first_row, second_row, third_row]

first_column = [first_row[0], second_row[0], third_row[0]]
second_column = [first_row[1], second_row[1], third_row[1]]
third_column = [first_row[2], second_row[2], third_row[2]]

diagonal1 = [first_row[0], second_row[1], third_row[2]]
diagonal2 = [first_row[2], second_row[1], third_row[0]]

for lists in magic_square:
        print (lists)

if sum(first_row) == sum(second_row) == sum(third_row) == sum(first_column) == sum (second_column) == sum (third_column) == sum(diagonal1) == sum(diagonal2):
    print ("This is a magic square!")
else:
    print ("This is not a magic square!")
    
