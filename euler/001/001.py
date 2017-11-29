#!/usr/bin/env python

def sum_multiples_of_3_or_5(below):
    s = 0
    for i in range(below):
        if (i % 3 == 0) or (i % 5 == 0):
            s += i
    return s

print "Sum of multiples of 3 or 5 below 10:  ", sum_multiples_of_3_or_5(10)
print "Sum of multiples of 3 or 5 below 1000:", sum_multiples_of_3_or_5(1000)
