D = int(input()) # number of starting doughnuts

E = int(input()) # number of events

# For that many events, run the loop...
for _ in range(E):
    symbol = input() # either + or -
    Q = int(input()) # number of doughnuts affected

    if symbol == '-':
        D -= Q
    elif symbol == '+':
        D += Q

print(D)
