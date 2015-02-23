from random import randint

def generate_random_list (n, start, end):
    random_list = []
    i = 0
    while i != n:
        random_list = random_list + [randint(start, end)]
        i += 1
    return random_list

n = input("Enter n: ")
n = int(n)

start = input("Enter start: ")
start = int(start)

end = input("Enter end: ")
end = int(end)

print (generate_random_list(n, start, end))
