# post-RLE
S = input()

# parse RLE
parsed = []

c = S[0]
n = ''
for i in range(1, len(S)):
    if S[i].isdigit():
        n += S[i]
    else:
        parsed.append((c, int(n)))
        c = S[i]
        n = ''

# final block
parsed.append((c, int(n)))

# index
c = int(input())

# find char at c-th index
i = 0
found = False
while not found:
    for (c, n) in parsed:
        i += n
        if i >= n:
            print(c)
            found = True
            break
