def join(delimeter, items):
    new_string = items[0]
    for i in range(1, len(items)):
        new_string = new_string + str(delimeter) + str(items[i])
    return new_string

def board_to_string(board):
    result = ''
    for row in board:
        result += "| " + str(join(" | ", row)) + " |" + "\n"
    
    return result

board = [ ["X", "O", "#"],
          ["X", "X", "X"],
          ["#", "#", "#"] ]

result = board_to_string(board)
print(result)
