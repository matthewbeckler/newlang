#!/usr/bin/env python

test_banks = [0, 2, 7, 0]
real_banks = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]

def cycle(banks):
    chosen = banks.index(max(banks))
    print banks, chosen
    count = banks[chosen]
    banks[chosen] = 0
    ix = chosen + 1
    for i in range(count):
        ix = ix % len(banks)
        banks[ix] += 1
        ix += 1
    return banks

def reallocate(banks):
    states = set()
    cycles = 0
    while True:
        banks = cycle(banks)
        cycles += 1
        if tuple(banks) in states:
            # found repeated state, we're done
            print "Repeated state:"
            print banks
            return cycles
        states.add(tuple(banks))

def reallocate_part_two(banks):
    states = {} # map from state to ix when last ween
    cycles = 0
    while True:
        banks = cycle(banks)
        cycles += 1
        if tuple(banks) in states.keys():
            # found repeated state, we're done
            print "Repeated state:"
            print banks
            return (cycles - states[tuple(banks)])
        states[tuple(banks)] = cycles


print reallocate(list(test_banks))
print reallocate(list(real_banks))

print reallocate_part_two(list(test_banks))
print reallocate_part_two(list(real_banks))

