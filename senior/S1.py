# Input is a set of four space-separated integers, e.g. 1 2 3 4
# Order: painting 1's base and height, then painting 2's base and height
values = input()
A, B, X, Y = (int(v) for v in values.split())

# Thinking through this...
# Evidently, the minimum area is when the paintings directly abut each other, with no gap in between.
# Moreover, it'll be optimal if one painting is entirely contained in one dimension of the other rectangle, either length or height (that is, they don't just touch at the corners or something).

# The optimal wall coverage will thus be the LONGEST dimension on one axis (the longer base or height), and the SUM of the dimensions on the other axis. See example #3 in the problem PDF for why this is the case. There, the rectangle is painting 2's base (3) by the combined heights of the paintings (1 + 2).

# We can just try making both arrangements (stack them horizontally or vertically) and see which is shorter, then output that.
# Note that they can't rotate, so we only need to compare base to base and height to height, not other combinations of those.

stack_bases = max(A, X) + B + Y
stack_heights = max(B, Y) + A + X

# Find the smaller way of stacking them
smaller = min((stack_bases, stack_heights))

# Don't forget that we only found one of each dimension (how tall and how wide it has to be)
# So double it for the perimeter
print(2 * smaller)