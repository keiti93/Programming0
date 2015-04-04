string = input("Enter string: ")
string = string.lower()

p_marks = [".", ",", "!", "?", "-", "_", ":", ";"]

def is_string_palindrome(string):
    new_string = ''
    is_palindrome = ''
    for letter in string:
        if (letter != " ") and letter not in p_marks:
            new_string += letter
            is_palindrome = letter + is_palindrome
    return (new_string == is_palindrome)
        
print (is_string_palindrome (string))
