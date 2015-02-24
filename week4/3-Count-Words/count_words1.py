def count_words(words):
    dictionary = {}
    count = 0
    i = 0
    for word in words:
        while i != len(words):
            if word == words[i]:
                count += 1
            i += 1
        dictionary[word] = count
        count = 0
        i = 0
    return dictionary
