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

def sum_freqs_part1(inputs):
    return sum(inputs)

# Unit Tests
test1 = [+1, -2, +3, +1]
test2 = [+1, +1, +1]
test3 = [+1, +1, -2]
test4 = [-1, -2, -3]

assert sum_freqs_part1(test1) == 3
assert sum_freqs_part1(test2) == 3
assert sum_freqs_part1(test3) == 0
assert sum_freqs_part1(test4) == -6

print("Solution to Part 1 is {}".format(sum_freqs_part1(inputs))) # 513

def find_first_repeat_freq(inputs):
    cum_sum = 0
    freqs_seen = {cum_sum}
    for x in cycle(inputs): # Cycle creates returns iterator to cycle through an iterable indefinitely
        cum_sum += x
        if cum_sum in freqs_seen:
            break
        freqs_seen.add(cum_sum)
    return cum_sum

test2_part2 = [1, -1]
test3_part2 = [+3, +3, +4, -2, -4]
test4_part2 = [-6, +3, +8, +5, -6]
test5_part2 = [+7, +7, -2, -7, -4]

assert find_first_repeat_freq(test1) == 2
assert find_first_repeat_freq(test2_part2) == 0
assert find_first_repeat_freq(test3_part2) == 10
assert find_first_repeat_freq(test4_part2) == 5
assert find_first_repeat_freq(test5_part2) == 14

print("Solution to Part 2 is {}".format(find_first_repeat_freq(inputs))) # 287
