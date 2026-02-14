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

def find_optimal_change() -> tuple[int, int]:
    """
    Check for an optimal change of the colour of one pen.
    Return a tuple [i, oc, nc] where the colour of the pen
    at index i is currently oc and should be changed to nc.
    If no change is desirable, oc == nc.

    A change is desirable when a given colour A
    will gain more prettiness than the loss to the other colour B.
    This would occur whenever A's maximum prettiness is lower than
    a prettiness available to B that is less than B's maximum prettiness.
    For example, if A has [2, 3] and B has [4, 6], if we swap the pen
    with 4 prettiness to A, our total prettiness is higher.
    
    To make it optimal, however, presumably we need to find said change
    that maximizes the total gain; that is, where there is the greatest
    difference between the highest prettiness of any colour A and the
    second-highest prettiness of any colour B.
    """

    # Defaults that won't affect anything if they don't get replaced
    change_i = 0
    change_oc = colours[0]
    change_nc = colours[0]

    # "best seen yet" algorithm
    greatest_difference = 0

    # Try each colour's best one
    for colour in range(1, M + 1):
        _, my_prettinesses = get_prettinesses_of_colour(colour)
        my_best = max(my_prettinesses)

        # Try all other colour that could be a donor... omitting this one... :)
        for donor in range(1, M + 1):
            if donor == colour:
                continue

            colour_indices, other_prettinesses = get_prettinesses_of_colour(donor)

            # If the donor colour has only one option, it can't donate
            if len(colour_indices) == 1:
                continue

            # Remove max to avoid swapping with it
            other_best = max(other_prettinesses)
            i_other_best = other_prettinesses.index(other_best)
            other_prettinesses.remove(other_best)
            del colour_indices[i_other_best]

            # Again now that the best has been removed
            other_best = max(other_prettinesses)
            i_prettiness = other_prettinesses.index(other_best)
            i_colour = colour_indices[i_prettiness]

            # Check the difference.
            difference = other_best - my_best
            if difference > greatest_difference:
                greatest_difference = difference
                change_i = i_colour
                change_oc = donor
                change_nc = colour
    
    return change_i, change_oc, change_nc

def get_prettinesses_of_colour(target_colour: int) -> tuple[list[int]]:
    """
    Gather the prettinesses of the pens of this colour.
    Return them along with a parallel list of their indices in the list of pens.
    """

    indices = []
    results = []

    for i in range(N):
        if colours[i] == target_colour:
            indices.append(i)
            results.append(prettinesses[i])

    return indices, results

def paint_picture() -> int:
    """
    Paint the current picture and return its prettiness.

    1. Check for an optimal change
    2. For each colour, paint using the prettiest pen, summing its prettiness
    3. Undo the optimal change
    4. Return the summed prettiness
    """

    # Get an optimal change. i, old colour, new colour
    change_i, change_oc, change_nc = find_optimal_change()
    colours[change_i] = change_nc

    # Paint the picture with the best prettiness of each colour of pen
    prettiness = 0

    # For each colour, find the prettiest pen and add it to the painting's prettiness
    for colour in range(1, M + 1):
        _, prettinesses = get_prettinesses_of_colour(colour)
        prettiness += max(prettinesses)

    # Revert the optimization change if one was made
    colours[change_i] = change_oc

    # Return painting's prettiness
    return prettiness

 # Actual program

print(paint_picture())

for i in range(Q):    

    # Make the next change from Q
    kind_of_change, i_change, new_value = changes[i]

    # 1-based again...
    i_change -= 1

    # 1 = change colour of i-th pen
    if kind_of_change == 1:
        colours[i_change] = new_value
    
    # 2 = change prettiness of i-th pen
    elif kind_of_change == 2:
        prettinesses[i_change] = new_value
    
    print(paint_picture())
