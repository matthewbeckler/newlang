#!/usr/bin/env python
# Day 18: Duet

from collections import deque

real = """set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 464
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19"""

test = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""

test_part_two = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""

def part_one(instrs):
    debug = False
    regs = {} # map from reg letter to value. Use regs.get(x, 0) to default to 0

    def get_val(val):
        """ If val is a number, return int(val).
            If val is a reg name, return reg[val]. """
        try:
            return int(val)
        except ValueError:
            return regs.get(val, 0)

    pc = 0
    while True:
        instr = instrs[pc]
        if debug: print regs
        if debug: print "===== PC=%d -> %s =====" % (pc, instr)
        items = instr.split()
        op = items[0]
        if op == "set":
            reg = items[1]
            val = get_val(items[2])
            regs[reg] = val
        elif op == "add":
            reg = items[1]
            val = get_val(items[2])
            regs[reg] = regs.get(reg, 0) + val
        elif op == "mul":
            reg = items[1]
            val = get_val(items[2])
            regs[reg] = regs.get(reg, 0) * val
        elif op == "mod":
            reg = items[1]
            val = get_val(items[2])
            regs[reg] = regs.get(reg, 0) % val
        elif op == "snd":
            regs["freq"] = get_val(items[1])
        elif op == "rcv":
            val = get_val(items[1])
            if val != 0:
                print "Hit non-zero RCV, freq is %d" % regs["freq"]
                break
        elif op == "jgz":
            valx = get_val(items[1])
            valy = get_val(items[2])
            if valx > 0:
                pc += (valy - 1) # PC will be incremented below, so sub 1 here

        pc += 1
    if debug: print regs


def part_two(instrs):
    debug = False
    regs_a = {"p": 0} # map from reg letter to value. Use regs.get(x, 0) to default to 0
    regs_b = {"p": 1}

    # use .append() and .popleft()
    queue_a2b = deque()
    queue_b2a = deque()

    prog_1_send = 0

    def get_val(val, regs):
        """ If val is a number, return int(val).
            If val is a reg name, return reg[val]. """
        try:
            return int(val)
        except ValueError:
            return regs.get(val, 0)
    def eval(pc, instr, regs, queue_snd, queue_rcv):
        """ Eval the instr and update the regs. Return (new PC, num values sent). """
        num_val_sent = 0
        items = instr.split()
        op = items[0]
        if op == "set":
            reg = items[1]
            val = get_val(items[2], regs)
            regs[reg] = val
        elif op == "add":
            reg = items[1]
            val = get_val(items[2], regs)
            regs[reg] = regs.get(reg, 0) + val
        elif op == "mul":
            reg = items[1]
            val = get_val(items[2], regs)
            regs[reg] = regs.get(reg, 0) * val
        elif op == "mod":
            reg = items[1]
            val = get_val(items[2], regs)
            regs[reg] = regs.get(reg, 0) % val
        elif op == "snd":
            val = get_val(items[1], regs)
            queue_snd.append(val)
            num_val_sent += 1
        elif op == "rcv":
            reg = items[1]
            if len(queue_rcv) == 0:
                # nothing in the queue, return current PC to try again
                return pc, num_val_sent
            # else, store received value
            regs[reg] = queue_rcv.popleft()
        elif op == "jgz":
            valx = get_val(items[1], regs)
            valy = get_val(items[2], regs)
            if valx > 0:
                pc += (valy - 1) # PC will be incremented below, so sub 1 here
        pc += 1
        return pc, num_val_sent

    pc_a = 0
    pc_b = 0
    deadlock_a = False
    deadlock_b = False
    prog_1_send = 0
    while True:
        # cpu A
        instr = instrs[pc_a]
        if debug: print "A:", regs_a
        if debug: print "===== PC_A = %d -> %s =====" % (pc_a, instr)
        pc_a_new, num_val_sent = eval(pc_a, instr, regs_a, queue_a2b, queue_b2a)
        deadlock_a = (pc_a == pc_a_new)
        pc_a = pc_a_new

        # cpu B
        instr = instrs[pc_b]
        if debug: print "B:", regs_b
        if debug: print "===== PC_B = %d -> %s =====" % (pc_b, instr)
        pc_b_new, num_val_sent = eval(pc_b, instr, regs_b, queue_b2a, queue_a2b)
        deadlock_b = (pc_b == pc_b_new)
        pc_b = pc_b_new
        prog_1_send += num_val_sent

        # check for global deadlock
        if deadlock_a and deadlock_b:
            print "Global deadlock detected, prog 1 sent %d values" % prog_1_send
            break

    if debug: print "A:", regs_a
    if debug: print "B:", regs_b


print "Part one test:"
part_one(test.split("\n"))

print "Part one real:"
part_one(real.split("\n"))

print "Part two test:"
part_two(test_part_two.split("\n"))

print "Part two real:"
part_two(real.split("\n"))
