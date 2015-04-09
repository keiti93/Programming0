def setify(a):
    result = []
     
    for item in a:
        if item not in result:
            result.append(item)
    return result
         
 
def diff(a, b):
    result = []
    for item in a:
        if item not in b:
            result.append(item)
    return setify(result)
 
def union(a, b):
    return setify(a+b)
 
def intersection(a, b):
    result = []
    for item in a:
        if item in b:
            result.append(item)
    return setify(result)
 
def cartesian_product(a, b):
    a = setify(a)
    b = setify(b)
    result = []
     
    for x in a:
        for y in b:
            result.append((x, y))
    return result
