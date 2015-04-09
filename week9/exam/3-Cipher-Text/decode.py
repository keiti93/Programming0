def reverse(d):
    result = {}
    for key in d:
        value = d[key]
        result[value] = key
    return result
 
def decode_word(encrypted_word, cipher):
    decoded_word = ''
    reversed_cipher = reverse(cipher)
 
    for ch in encrypted_word:
        if ch in reversed_cipher:
            decoded_word += reversed_cipher[ch]
    return decoded_word
        
