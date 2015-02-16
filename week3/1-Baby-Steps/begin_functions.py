def square(x):
    return x**2

def fact(x):
    start = 1
    sum = 1
    while start <= x:
        sum = sum*start
        start += 1
    return sum

def count_elements(items):
    count = 0
    for element in items:
        count += 1
    return count

def member(x, xs):
    a = False
    for item in xs:
        if x == item:
            a = True
            break
    return a


def grades_that_pass(students, grades, limit):
    list1 = []
    index = 0
    for grade in grades:
        if grade >= limit:
            list1 = list1 + [students[index]]
        index += 1
    return list1
