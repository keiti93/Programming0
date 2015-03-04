def magic_square(square):
    
    if (sum(square[0]) == sum(square[1])) and (sum(square[1]) == sum(square[2])):
        return True
    
    return False
