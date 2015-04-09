def setify(a):
    result = []
     
    for item in a:
        if item not in result:
            result.append(item)
    return result
 
def second_largest(numbers):
    sorted_numbers = setify(sorted(numbers, reverse=True))
    if (len(sorted_numbers)==0) or (len(sorted_numbers)==1):
        return False
    return sorted_numbers[1]
