def sublist(list1, list2):

    if list1==[] and list2==[]:
        return True

    if len(list1)==len(list2):
        for number in range(0, len(list1)):
            if list1[number] != list2[number]:
                return False
        else:
            return True

    if len(list1) > len(list2):
        return False

    index = 0
    while index < len(list2):
        if list1[0] == list2[index]:
            n = index
            x = index
            for number in range(0, len(list1)):
                if list1[number] == list2[n]:
                    n += 1
            if n - x == len(list1):
                return True
        index += 1

    return False

