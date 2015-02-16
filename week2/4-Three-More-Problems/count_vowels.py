n = input ("Enter string: ")

vowel_counter = 0
vowels = "aeiouyAEIOUY"

for ch in n:
    if ch in vowels:
        vowel_counter += 1

print (n, "-", vowel_counter)
