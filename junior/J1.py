N = int(input()) # your place in line
C = int(input()) # number of cars
P = int(input()) # number of people per car

# the train's capacity is number of cars times number of people per car
# if your place in line is within that amount, you'll be on the next train

if (C * P) >= N:
    print('yes')
else:
    print('no')
