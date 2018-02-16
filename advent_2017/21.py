#!/usr/bin/env python
# Day 21: Fractal Art

import pprint

rules_test_2 = {
    "../.#": "##./#../...",
}
rules_test_3 = {
    ".#./..#/###": "#..#/..../..../#..#",
}

# string indices for the 8 rotations/flips
# flips are left/right flips by convention, but we still get all 8 arrangements
mapping_2 = [
    [0, 1, 2, 3, 4], # NO  rotation, NO flip
    [1, 0, 2, 4, 3], # NO  rotation, LR flip
    [1, 4, 2, 0, 3], # CCW rotation, NO flip
    [4, 1, 2, 3, 0], # CCW rotation, LR flip
    [3, 0, 2, 4, 1], # CW  rotation, NO flip
    [0, 3, 2, 1, 4], # CW  rotation, LR flip
    [4, 3, 2, 1, 0], # 180 rotation, NO flip
    [3, 4, 2, 0, 1], # 180 rotation, LR flip
]
mapping_3 = [
    [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10], # NO  rotation, NO flip
    [ 2,  1,  0,  3,  6,  5,  4,  7, 10,  9,  8], # NO  rotation, LR flip
    [ 2,  6, 10,  3,  1,  5,  9,  7,  0,  4,  8], # CCW rotation, NO flip
    [10,  6,  2,  3,  9,  5,  1,  7,  8,  4,  0], # CCW rotation, NO flip
    [ 8,  4,  0,  3,  9,  5,  1,  7, 10,  6,  2], # CW  rotation, NO flip
    [ 0,  4,  8,  3,  1,  5,  9,  7,  2,  6, 10], # CW  rotation, NO flip
    [10,  9,  8,  3,  6,  5,  4,  7,  2,  1,  0], # 180 rotation, NO flip
    [ 8,  9, 10,  3,  4,  5,  6,  7,  0,  1,  2], # 180 rotation, NO flip
]

def iterate(square):
    """ Return all 8 rotated/flipped variants of the input square. """
    if len(square) == 5:
        mapping = mapping_2
    else:
        mapping = mapping_3

    ret = []
    for m in mapping:
        ret.append("".join([square[x] for x in m]))
    return ret

#print "\n".join(iterate(".#/##"))
#print "\n".join(iterate(".#./..#/###"))

def expand_rules(rules):
    ret = {}
    for i, o in rules.iteritems():
        expanded_i = iterate(i)
        for ei in expanded_i:
            ret[ei] = o
    return ret

expanded_rules_test = expand_rules(rules_test_2)
expanded_rules_test.update(expand_rules(rules_test_3))
#pprint.pprint(expanded_rules_test)

# TODO remove
def find_match(square, rules):
    assert square in rules
    return rules[square]

def extract(square, ix, iy, dim):
    """ Extract the dimXdim square at offset ix, iy. x increases to the right, y increases to the top, like math. """
    width = square.find("/")
    # go row-by-row
    rows = []
    #print "width %d, square:" % width
    #print square
    for d in range(dim):
        i = ix + ((iy + d) * (width + 1))
        #print "ix %d, iy %d, d %d, i %d" % (ix, iy, d, i)
        rows.append(square[i:i+dim])
    ret = "/".join(rows)
    #print ret
    return ret
assert extract("#..#/..../..../#..#", 0, 0, 2) == "#./.."
assert extract("#..#/..../..../#..#", 2, 0, 2) == ".#/.."
assert extract("#..#/..../..../#..#", 0, 2, 2) == "../#."
assert extract("#..#/..../..../#..#", 2, 2, 2) == "../.#"
assert extract("#..#/..../..../#..#", 0, 0, 3) == "#../.../..."

iterations = 2
square = ".#./..#/###"
for ix in range(iterations):
    print "\n===== %d =====" % ix
    width = square.find("/")
    if width % 2 == 0:
        print "div by 2"
    elif width % 3 == 0:
        print "div by 3"
    else:
        assert 0
    print find_match(".#./..#/###", expanded_rules_test)

