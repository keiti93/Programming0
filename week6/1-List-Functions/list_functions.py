def head(a):
    if a == []:
        return None
    return a[0]

def last(a):
    if a == []:
        return None
    return a[len(a)-1]

def tail(a):
    new_list = []
    for i in range (1, len(a)):
        new_list = new_list + [a[i]]
    return new_list

def equal_lists(a,b):
    if len(a)==len(b):
        for i in range (0, len(a)):
            if a[i]==b[i]:
                return True
    return False

def count_item(x, a):
    counter = 0
    for element in a:
        if element == x:
            counter += 1
    return counter

def take (n, a):
    new_list = []
    for i in range (0, n):
        if n > len(a):
            return a
        else:     
            new_list = new_list + [a[i]]
    return new_list

def drop (n, a):
    new_list = []
    for i in range (n, len(a)):
        new_list = new_list + [a[i]]
    return new_list

def reverse (a):
    new_list = []
    for i in range (len(a)-1, -1, -1):
        new_list = new_list + [a[i]]
    return new_list
