#!/usr/bin/env python
# Day 14: Disk Defragmentation

import sys
import operator

def knot_hash_round(elems, lens, ix, skip_size):
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

def knot_hash(lens):
    lens.extend([17, 31, 73, 47, 23])
    elems = range(256)
    ix = 0
    skip_size = 0
    for i in range(64):
        elems, ix, skip_size = knot_hash_round(elems, lens, ix, skip_size)
    #print "Sparse hash:", elems
    #print "len:", len(elems)
    assert set(elems) == set(range(256))
    # now reduce the hash
    densehash = []
    for ix in range(16):
        densehash.append(reduce(operator.xor, elems[0 + (ix * 16):16 + (ix * 16)]))
    #print "Dense hash:", densehash
    #print "".join(map(lambda x: "%02x" % x, densehash))
    return densehash

def count_ones(b):
    lut = {
        0: 0,
        1: 1,
        2: 1,
        3: 2,
        4: 1,
        5: 2,
        6: 2,
        7: 3,
        8: 1,
        9: 2,
        10: 2,
        11: 3,
        12: 2,
        13: 3,
        14: 3,
        15: 4,
    }
    assert 0 <= b <= 255
    n1 = b & 0xf
    n2 = b >> 4
    return lut[n1] + lut[n2]
assert count_ones(15) == 4
assert count_ones(0xA5) == 4


def part_one(key):
    used = 0
    data = [] # list of lists of 0 (free) / 1 (used) values
    for i in range(128):
        this_key = key + "-{0:d}".format(i)
        kh = knot_hash(map(ord, this_key))
        #print this_key
        #print kh
        row = []
        for byte in kh:
            for bit in range(7, -1, -1):
                if byte & (1 << bit):
                    used += 1
                    row.append(1)
                else:
                    row.append(0)
        #print "".join(map(lambda c: "#" if c == 1 else ".", row))
        data.append(row)
    print "'%s' -> %d used" % (key, used)
    return data
        
def part_two(data):
    """ Determine how many (U/D/L/R) connected regions there are. """
    regions = [] # 0 is unused, assign values to indicate which region
    for i in range(128):
        regions.append([0] * 128)
    # try each point, if it's used an not in a region, follow any neighbors
    next_region_id = 1
    # coordinates are [y][x], with y[0] being the top row, and x[0] being the left column
    for iy in range(128):
        for ix in range(128):
            #print "====== (y=%d, x=%d) ======" % (iy, ix)
            if data[iy][ix] == 0:
                #print "  block is not used"
                continue
            if regions[iy][ix] != 0:
                #print "  already part of a region"
                continue
            # Else, the block is in use but not already in a region
            # We can assume that this block is unconnected to any other
            # already-explored region (otherwise it'd have been explored already).
            todo = set()
            todo.add((iy, ix))
            while len(todo) > 0:
                #print "  === todo: %s ===" % str(todo)
                pt = todo.pop()
                #print "    %s" % str(pt)
                pty = pt[0]
                ptx = pt[1]
                regions[pty][ptx] = next_region_id
                # add neighbors that exist, are in use, but not yet in a region
                if ptx > 0 and data[pty][ptx - 1] != 0 and regions[pty][ptx - 1] == 0:
                    #print "    Adding (y=%d, x=%d) on left" % (pty, ptx - 1)
                    todo.add((pty, ptx - 1))
                if ptx < 127 and data[pty][ptx + 1] != 0 and regions[pty][ptx + 1] == 0:
                    #print "    Adding (y=%d, x=%d) on right" % (pty, ptx + 1)
                    todo.add((pty, ptx + 1))
                if pty > 0 and data[pty - 1][ptx] != 0 and regions[pty - 1][ptx] == 0:
                    #print "    Adding (y=%d, x=%d) on top" % (pty - 1, ptx)
                    todo.add((pty - 1, ptx))
                if pty < 127 and data[pty + 1][ptx] != 0 and regions[pty + 1][ptx] == 0:
                    #print "    Adding (y=%d, x=%d) on bottom" % (pty + 1, ptx)
                    todo.add((pty + 1, ptx))
            next_region_id += 1
        print "".join(map(lambda c: "%X"%(c % 16) if c != 0 else ".", regions[iy]))
    print "next id: %d, so this has %d regions" % (next_region_id, next_region_id - 1)

                
            

data_test = part_one("flqrgnkx")
data_real = part_one("xlqgujun")

part_two(data_test)
part_two(data_real)
