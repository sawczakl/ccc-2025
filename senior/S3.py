vals = input()

N, M, Q = (int(v) for v in vals.split())

pen_colours = []
pen_prettinesses = []

for _ in range(N):
    vals = input()
    C, P = (int(v) for v in vals.split())
    pen_colours.append(C)
    pen_prettinesses.append(P)

changes = []

for _ in range(Q):
    vals = input()
    kind, i, new = (int(v) for v in vals.split())
    changes.append((kind, i, new))

def paint_picture(i) -> int:
    pass

total_prettiness = 0

for i in range(1, Q + 1):
    total_prettiness += paint_picture(i)

print(paint_picture)
