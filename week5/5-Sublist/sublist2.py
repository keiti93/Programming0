def take(n, a):
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

def sublist(list1, list2):
    n = len(list1)
    while len(list2) != 0:
        if take(n, list2) == list1:
            return True
        list2 = drop(1, list2)

    return False
