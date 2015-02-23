n = input ("Enter number of blocks: ")
n = int(n)

blocks = []
count = 1

while count <= n:

    block = input()
    block = int(block)
    count += 1
    blocks = blocks + [block]

seen_blocks = 1
tallest_block = blocks[0]

for block in blocks:
    if block > tallest_block:
        tallest_block = block
        seen_blocks +=1

print ("You can see", seen_blocks, "blocks.")
