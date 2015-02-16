n = input ("Enter n: ")
n = int(n)

names = []
count = 1

while count <= n:
    name = input()
    count += 1
    names = names + [name]

names = sorted(names)

for i in names:
    print(i)
