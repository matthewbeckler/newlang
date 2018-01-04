#!/usr/bin/env python

test = [
    (1, 0),
    (12, 3),
    (23, 2),
    (1024, 31)
]

test_coords = [
    ( 1, ( 0, 0)),
    ( 2, ( 1, 0)),
    ( 3, ( 1, 1)),
    ( 4, ( 0, 1)),
    ( 5, (-1, 1)),
    ( 6, (-1, 0)),
    ( 7, (-1,-1)),
    ( 8, ( 0,-1)),
    ( 9, ( 1,-1)),
    (10, ( 2,-1)),
    (11, ( 2, 0)),
    (12, ( 2, 1)),
    (13, ( 2, 2)),
    (14, ( 1, 2)),
    (15, ( 0, 2)),
    (16, (-1, 2)),
    (17, (-2, 2)),
    (18, (-2, 1)),
    (19, (-2, 0)),
    (20, (-2,-1)),
    (21, (-2,-2)),
    (22, (-1,-2)),
    (23, (0,-2))
]

def count_steps(x):
    # keep track of the most extrme values we've seen so far,
    # that tells us when to turn
    mins = [0, 0]
    maxs = [0, 0]
    coord = [0, 0]
    vel = [1, 0] # direction we are moving

    nextvel = {
        ( 1,  0): ( 0,  1),
        ( 0,  1): (-1,  0),
        (-1,  0): ( 0, -1),
        ( 0, -1): ( 1,  0)
    }

    for i in range(2, x+1):
        # move to new coord
        old = coord
        coord[0] += vel[0]
        coord[1] += vel[1]
        #print "%d, c%s += v%s ==> c%s" % (i, old, vel, coord)
        # check if we need to turn
        turn = False
        if vel[0] != 0:
            # moving in x
            if coord[0] > maxs[0]:
                turn = True
                maxs[0] = coord[0] 
            if coord[0] < mins[0]:
                turn = True
                mins[0] = coord[0]
        elif vel[1] != 0:
            # moving in y
            if coord[1] > maxs[1]:
                turn = True
                maxs[1] = coord[1]
            if coord[1] < mins[1]:
                turn = True
                mins[1] = coord[1] 
        if turn:
            #print "Turn"
            vel = nextvel[tuple(vel)]
    return coord


def part_two(i):
    # keep track of the most extreme values we've seen so far,
    # that tells us when to turn
    mins = [0, 0]
    maxs = [0, 0]
    coord = [0, 0]
    vel = [1, 0] # direction we are moving

    nextvel = {
        ( 1,  0): ( 0,  1),
        ( 0,  1): (-1,  0),
        (-1,  0): ( 0, -1),
        ( 0, -1): ( 1,  0)
    }

    data_store = {} # map from (x,y) to stored value or 0
    data_store[(0,0)] = 1

    for ix in range(2, i+1):
        # move to new coord
        old = coord
        coord[0] += vel[0]
        coord[1] += vel[1]
        s = sum([data_store.get((x,y),0) for x in range(coord[0]-1, coord[0]+2) for y in range(coord[1]-1, coord[1]+2)])
        data_store[tuple(coord)] = s
        print "%d, c%s += v%s ==> c%s (value %d)" % (ix, old, vel, coord, s)
        if s > i:
            print "Found a new value higher than input i"
            print s
            return



        # check if we need to turn
        turn = False
        if vel[0] != 0:
            # moving in x
            if coord[0] > maxs[0]:
                turn = True
                maxs[0] = coord[0] 
            if coord[0] < mins[0]:
                turn = True
                mins[0] = coord[0]
        elif vel[1] != 0:
            # moving in y
            if coord[1] > maxs[1]:
                turn = True
                maxs[1] = coord[1]
            if coord[1] < mins[1]:
                turn = True
                mins[1] = coord[1] 
        if turn:
            #print "Turn"
            vel = nextvel[tuple(vel)]
    return coord


for i, coord in test_coords:
    answer = count_steps(i)
    if answer[0] != coord[0] or answer[1] != coord[1]:
        print "  FAIL"
    else:
        print "  PASS"

x = 325489
answer = count_steps(x)
print abs(answer[0]) + abs(answer[1])

part_two(x)
