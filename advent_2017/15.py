#!/usr/bin/env python
# Day 15: Dueling Generators

def gen(cur, factor, must_be_mult_of):
    n = cur
    while True:
        n = (n * factor) % 2147483647
        if (n % must_be_mult_of) == 0:
            return n

def part_one(seeds, factors):
    a = seeds[0]
    b = seeds[1]
    matches = 0
    for i in range(40000000):
        a = gen(a, factors[0], 1)
        b = gen(b, factors[1], 1)
        #print "%12d, %12d" % (a, b)
        if a & 0xffff == b & 0xffff:
            matches += 1
    print matches

def part_two(seeds, factors):
    a = seeds[0]
    b = seeds[1]
    matches = 0
    for i in range(5000000):
        a = gen(a, factors[0], 4)
        b = gen(b, factors[1], 8)
        #print "%12d, %12d" % (a, b)
        if a & 0xffff == b & 0xffff:
            matches += 1
    print matches

factors = (16807, 48271)

seeds_test = (65, 8921)
seeds_real = (679, 771)

print "Part one, test:"
part_one(seeds_test, factors)
print "Part two, real:"
part_one(seeds_real, factors)

print "Part two, test:"
part_two(seeds_test, factors)
print "Part two, real:"
part_two(seeds_real, factors)
