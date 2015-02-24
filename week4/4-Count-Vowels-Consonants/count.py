def count_vowels_consonants(word):
    count_vowels = 0
    count_consonants = 0
    vowels = "aeiouyAEIOUY"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    
    for letter in word:
        if letter in vowels:
            count_vowels +=1
        elif letter in consonants:
            count_consonants +=1
        else:
            print ("This is not a normal word!")

    dictionary = {"vowels" : count_vowels,
                  "consonants" : count_consonants}
    return dictionary
