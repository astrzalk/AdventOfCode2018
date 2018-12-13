#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Puzzle found at: https://adventofcode.com/2018/day/1

from itertools import cycle

# Read Inputs
file_name = "day01_input.txt"
inputs = []
with open(file_name) as f:
    for num in f:
        num = int(num.strip('\n'))
        inputs.append(num)

assert sum([+1, -2, +3, +1]) == 3
assert sum([+1, +1, +1]) == 3
assert sum([+1, +1, -2]) == 0
assert sum([-1, -2, -3]) == -6

print("Solution to Part 1 is {}".format(sum(inputs))) # 513

def find_first_repeat_freq(inputs):
    cum_sum = 0
    freqs_seen = {cum_sum}
    for x in cycle(inputs): # Cycle creates returns iterator to cycle through an iterable indefinitely
        cum_sum += x
        if cum_sum in freqs_seen:
            return cum_sum
        freqs_seen.add(cum_sum)

assert find_first_repeat_freq([+1, -2, +3, +1]) == 2
assert find_first_repeat_freq([1, -1]) == 0
assert find_first_repeat_freq([+3, +3, +4, -2, -4]) == 10
assert find_first_repeat_freq([-6, +3, +8, +5, -6]) == 5
assert find_first_repeat_freq([+7, +7, -2, -7, -4]) == 14

print("Solution to Part 2 is {}".format(find_first_repeat_freq(inputs))) # 287
