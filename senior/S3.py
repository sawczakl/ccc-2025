vals = input()

N, M, Q = (int(v) for v in vals.split())

colours = []
prettinesses = []

# Read the pen colours and prettinesses
for _ in range(N):
    vals = input()
    C, P = (int(v) for v in vals.split())
    colours.append(C)
    prettinesses.append(P)

# Store the changes for now
changes = []
for _ in range(Q):
    vals = input()
    changes.append((int(v) for v in vals.split()))

def paint_picture(i) -> int:

    # Check if there's an optimization change to make

    # Paint the picture with the best prettiness of each colour of pen
    prettiness = 0

    # For each colour
    for i_colour in range(M):

        # Gather the prettinesses of the pens of this colour
        pens_of_this_colour = []
        for j in range(len(colours)):
            if colours[j] == i_colour:
                pens_of_this_colour.append(prettinesses[j])

        # Add the highest prettiness to the painting's prettiness
        prettiness += max(pens_of_this_colour)

    # Revert the optimization change if one was made
    pass

    # Return painting's prettiness
    return prettiness

total_prettiness = 0

for i in range(Q):
    total_prettiness += paint_picture(i)
    
    # Make the next change from Q
    kind_of_change, i_change, new_value = changes[i]

    # 1 = change colour of i-th pen
    if kind_of_change == 1:
        colours[i_change] = new_value
    
    # 2 = change prettiness of i-th pen
    elif kind_of_change == 2:
        prettinesses[i_change] = new_value


print(paint_picture)
