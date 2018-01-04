#!/usr/bin/env python

import operator

test_input_size = 5
test_input_lens = [3, 4, 1, 5]

real_input_size = 256
real_input_lens = [129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108]

part_two_input_ascii = "129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108"

def part_one(elems, lens, ix, skip_size):
    for l in lens:
        #print "===== %s, ix %4d, skip_size %4d, len %4d =====" % (elems, ix, skip_size, l)
        sel = []
        for i in range(ix, ix+l):
            sel.append(elems[i % len(elems)])
        #print "sel:", sel
        for i in range(ix, ix+l):
            elems[i % len(elems)] = sel.pop()
            # todo is this right?
        ix = (ix + l + skip_size) % len(elems)
        skip_size += 1
    return (elems, ix, skip_size)

def part_two(lens):
    lens.extend([17, 31, 73, 47, 23])
    elems = range(256)
    ix = 0
    skip_size = 0
    for i in range(64):
        elems, ix, skip_size = part_one(elems, lens, ix, skip_size)
    print "Sparse hash:", elems
    print "len:", len(elems)
    assert set(elems) == set(range(256))
    # now reduce the hash
    densehash = []
    for ix in range(16):
        densehash.append(reduce(operator.xor, elems[0 + (ix * 16):16 + (ix * 16)]))
    print "Dense hash:", densehash
    print "".join(map(lambda x: "%02x" % x, densehash))




elems = range(test_input_size)
elems, ix, skip_size = part_one(elems, test_input_lens, 0, 0)
print "===== %s =====" % elems
print elems[0] * elems[1]

elems = range(real_input_size)
elems,ix, skip_size = part_one(elems, real_input_lens, 0, 0)
print "===== %s =====" % elems
print elems[0] * elems[1]

print "==== Part two: ====="
part_two(map(ord, ""))
part_two(map(ord, "AoC 2017"))
part_two(map(ord, "1,2,3"))
part_two(map(ord, "1,2,4"))
part_two(map(ord, part_two_input_ascii))
