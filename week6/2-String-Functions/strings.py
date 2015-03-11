def str_reverse(word):
    new_word = ""
    for i in range (len(word)-1, -1, -1):
        new_word = new_word + word[i]
    return new_word

def join(delimeter, items):
    new_string = items[0]
    for i in range(1, len(items)):
        new_string = new_string + str(delimeter) + str(items[i])
    return new_string

def startswith(search, string):
    n = len(search)
    new_string = ''
    if len(search)>len(string):
        return "The searched string is longer than the given string"
    for i in range (0, n):
        new_string += string[i]
    if search == new_string:
        return True
    return False

def endswith(search, string):
    n = len(search)
    new_string = ''
    if len(search)>len(string):
        return "The searched string is longer than the given string"
    for i in range (len(string)-n, len(string)):
        new_string += string[i]
    if search == new_string:
        return True
    return False



def tail(string):
    new_string = ''
    for i in range (1, len(string)):
        new_string += string[i]
    return new_string

def head (string):
    new_string = ''
    for i in range(0, len(string)-1):
        new_string += string[i]
    return new_string

def trim(string):
    new_string = string
    while startswith(" ", new_string):
        new_string = tail(new_string)
        if new_string == " ":
            return ''
    while endswith(" ", new_string):
        new_string = head(new_string)
    return new_string
