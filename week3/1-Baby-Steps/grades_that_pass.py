number = input("Enter number of students: ")
number = int(number)
students = []
grades = []
x = 1

print ("Enter names:")
while x<= number:
    n = input()
    students = students + [n]
    x +=1
x = 1

print ("Enter grades:")
while x<= number:
    m = input()
    m = float(m)
    grades = grades + [m]
    x += 1
print (students)
print (grades)

def grades_that_pass(students, grades, limit):
    list1 = []
    index = 0
    for grade in grades:
        if grade >= limit:
            list1 = list1 + [students[index]]
        index += 1
    return list1

result = grades_that_pass(students, grades, 4.0)
print (result)
