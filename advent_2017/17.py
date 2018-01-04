#!/usr/bin/env python
# Day 17: Spinlock

def print_state(state, pos):
    items = []
    for i in range(len(state)):
        if i == pos:
            items.append("(%d)" % state[i])
        else:
            items.append(" %d " % state[i])
    print " ".join(items)

def part_one(steps, stop_value):
    state = [0]
    pos = 0
    #print_state(state, pos)
    for i in range(1, stop_value + 1):
        if i % 50000 == 0:
            print i, i / (1.0 * stop_value)
        #print "i %d, pos %d" % (i, pos)
        # step forward
        pos = (pos + steps) % len(state)
        #print "new pos %d" % pos
        # insert a new value
        state.insert(pos + 1, i)
        pos += 1
        #print "new pos %d" % pos
        #print_state(state, pos)
    print "context around stop value:", state[pos-3:pos+4]
    return state

# for part two, only need the value after zero
# 0 always lives at pos=0
def part_two(steps, stop_value):
    size = 1
    pos = 0
    one_after_zero = 0
    #print_state(state, pos)
    for i in range(1, stop_value + 1):
        if i % 50000 == 0:
            print "i %d, pos %d" % (i, pos)
        # step forward
        pos = (pos + steps) % size
        #print "new pos %d" % pos

        # insert a new value
        if pos == 0:
            one_after_zero = i
        #state.insert(pos + 1, i)
        size += 1
        pos += 1
        #print "new pos %d" % pos
        #print_state(state, pos)
    print one_after_zero

    
part_one(3, 2017)
part_one(363, 2017)

part_two(363, 50000000)
