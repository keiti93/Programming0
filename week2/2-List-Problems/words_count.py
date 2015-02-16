w = input ("Enter word: ")
n = input ("Enter n: ")
n = int(n)

words = []
count = 1
times = 0

while count <= n:
    word = input()
    count += 1
    words = words + [word]
    
for word in words:
    if w == word:
        times = times + 1

print (w, "is found", times, "times." )
