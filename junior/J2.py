# starting doughnuts
D = int(input())
R = D

# events
E = int(input())

for _ in range(E):
    symbol = input()
    Q = int(input())

    if symbol == '-':
        R -= Q
    elif symbol == '+':
        R += Q

print(R)
