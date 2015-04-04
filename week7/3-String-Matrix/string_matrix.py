def take(n, string):
    new_string = ''

    for index in range(0, min(n, len(string))):
        new_string += string[index]
        
    return new_string

def string_matrix(matrix_width, strings):
    result = ''
    
    for i in range(0, matrix_width):
        for j in range(0, matrix_width):
            if len(strings[i]) > matrix_width:
                strings[i] = take(matrix_width, strings[i])
            if len(strings[i]) < matrix_width:
                while len(strings[i]) != matrix_width:
                    strings[i] += "X"
            if len(strings[i]) == matrix_width:
                for ch in strings[i][j]:
                    if j < (matrix_width - 1):
                        result += "| " + strings[i][j] + " "
                    else:
                        result += "| " + strings[i][j] + " |" + "\n"

    return print (result)
