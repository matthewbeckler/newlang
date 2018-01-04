#!/usr/bin/env python

test = """0: 3
1: 2
4: 4
6: 4"""

real ="""0: 4
1: 2
2: 3
4: 4
6: 8
8: 5
10: 8
12: 6
14: 6
16: 8
18: 6
20: 6
22: 12
24: 12
26: 10
28: 8
30: 12
32: 8
34: 12
36: 9
38: 12
40: 8
42: 12
44: 17
46: 14
48: 12
50: 10
52: 20
54: 12
56: 14
58: 14
60: 14
62: 12
64: 14
66: 14
68: 14
70: 14
72: 12
74: 14
76: 14
80: 14
84: 18
88: 14"""

def parse(string):
    data = {} # map from depth to range
    for row in string.split("\n"):
        d, r = map(int, row.split(": "))
        data[d] = r
    return data

def scanner_position(r, ix):
    """ Compute scanner position at time ix with range r. """
    mod_r = (2 * r) - 2
    pos = ix % mod_r
    #print "r = %d, ix = %d, pos = %d" % (r, ix, pos)
    if pos >= r:
        #print "bounce back, %d, %d" % (mod_r, ix)
        # ix:  0 1 2 3 4 5 6 7 8 9 A
        # r=3: 0 1 2 3|0 1 2 3|0 1 2 - mod_r = 4
        #      0 1 2 1|0 1 2 1|0 1 2
        # r=5: 0 1 2 3 4 5 6 7|0 1 2 - mod_r = 8
        #      0 1 2 3 4 3 2 1|0 1 2
        pos = (mod_r - pos)
    return pos

#for i in range(10):
#    print "%2d, %2d, %2d" % (i, scanner_position(3, i), scanner_position(5, i))

def traverse(data, start_ix):
    ever_caught = False
    severity = 0
    for ix in data.keys():
        # we get to layer ix at time ix + start_ix
        # scanner position is unfortunately not ix % range since it moves back-and-forth
        sp = scanner_position(data[ix], start_ix + ix)
        #print "ix %2d, sp %2d" % (ix, sp)
        if sp == 0:
            #print "  caught, severity = %d" % (ix * data[ix])
            ever_caught = True
            severity += (ix * data[ix])


    return ever_caught, severity

data_test = parse(test)
ever_caught, severity_test = traverse(data_test, 0)
print "Test: severity = %d" % severity_test

data_real = parse(real)
ever_caught, severity_real = traverse(data_real, 0)
print "Real: severity = %d" % severity_real

print "Part two: delay until we can get through uncaught"
delay = 0
while True:
    ever_caught, severity = traverse(data_real, delay)
    if ever_caught == False:
        break
    delay += 1
print "Got through uncaught with delay %d" % delay
