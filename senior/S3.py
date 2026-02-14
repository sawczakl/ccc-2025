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

    # Check if there's an optimization change to make.
    # We can change the colour of one pen.

    # A change is desirable when a given colour (A)
    # will gain more prettiness than the loss to the other colour (B).
    # This would occur whenever A's maximum prettiness is lower than
    # a prettiness available to B that is less than B's maximum prettiness.
    # For example, if A has [2, 3] and B has [4, 6], if we swap the pen
    # with 4 prettiness to A, our total prettiness is higher.
    
    # To make it optimal, however, presumably we need to find said switch
    # that maximizes the total gain; that is, where there is the greatest
    # difference between the highest P of any colour A and the non-highest
    # P of any colour B.

    # Check for an optimal change. Return a tuple [i, oc, nc] where the colour
    # at index i is currently oc and should be changed to nc.
    # If no change is desirable, oc == nc.

    # Defaults that won't affect anything if they don't get replaced
    change_i = 0
    change_oc = colours[0]
    change_nc = colours[0]

    greatest_difference = 0

    # Try each colour's best one
    for colour in range(M):
        _, my_prettinesses = get_prettinesses_of_colour(colour)
        my_best = max(my_prettinesses)

        # Try all other colour that could be a donor... omitting this one... :)
        for donor in range(M):
            if donor == colour:
                continue

            # If the donor colour has only one option, it can't donate
            if len(other_prettinesses) == 1:
                continue

            indices, other_prettinesses = get_prettinesses_of_colour(donor)

            # Remove max to avoid swapping with it
            # TODO I *think* this is good? That swapping with the max would not make sense?...          
            other_prettinesses.remove(max(other_prettinesses)) # NB in Python this only removes one instance, so if there are duplicates, we're good
            best_candidate = max(other_prettinesses)
            i_prettiness = other_prettinesses.index(best_candidate)
            i_colour = indices[i_prettiness]

            difference = best_candidate - my_best
            if difference > greatest_difference:
                greatest_difference = difference
                change_i = i_colour
                change_oc = colour
                change_nc = donor
    
    return change_i, change_oc, change_nc            

def get_prettinesses_of_colour(target_colour: int) -> tuple[list[int]]:

    # Gather the prettinesses of the pens of this colour
    # Return them along with a parallel list of their indices

    indices = []
    prettinesses = []

    for i in range(len(colours)):
        if colours[i] == target_colour:
            indices.append[i]
            prettinesses.append(prettinesses[i])

    return indices, prettinesses

def paint_picture(i) -> int:

    # Get an optimal change. i, old colour, new colour
    change_i, change_oc, change_nc = find_optimal_change()
    colours[change_i] = change_nc

    # Paint the picture with the best prettiness of each colour of pen
    prettiness = 0

    # For each colour, find the prettiest pen and add it to the painting's prettiness
    for colour in range(M):
        _, prettinesses = get_prettinesses_of_colour(colour)
        prettiness += max(prettinesses)

    # Revert the optimization change if one was made
    colours[change_i] = change_oc

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

print(total_prettiness)
