def sum_row(square):
    general_sum = sum(square[0])
    sum_r = 0
            
    for element in square:
        if sum(element)!= general_sum:
            return False
    return True

def sum_col(square):
    general_sum = sum(square[0])
    sum_column = 0
            
    for i in range (0, len(square)):
        for j in range (0, len(square)):
            sum_column += square[j][i]
        if sum_column != general_sum:
            return False
        else:
            sum_column = 0
    return True

def sum_d1(square):
    general_sum = sum(square[0])
    sum_d = 0
    
    for i in range (0, len(square)):
        sum_d += square[i][i]
    if sum_d != general_sum:
        print(sum_d)
        return False
    return True

def sum_d2(square):
    general_sum = sum(square[0])
    sum_d = 0
    i = len(square) - 1
    j = 0
    
    while i > -1:
        sum_d += square[i][j]
        i -= 1
        j += 1

    if sum_d != general_sum:
        return False
    return True

def magic_square(square):
    if sum_row(square) and sum_col(square) and sum_d1(square) and sum_d2(square):
        return True
    return False
    

