#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Dict, List, Tuple

with open('day02_input.txt') as f:
    inputs = [line.strip() for line in f]

## Part 1
def get_counts(s: str) -> Dict[str, int]:
    d = dict()
    for l in s:
        d[l] = d.get(l, 0) + 1
    return d

def get_checksum(inputs: List[str]) -> int:
    two_cnt, three_cnt = 0, 0
    for s in inputs:
        cnts = get_counts(s)
        if 2 in cnts.values():
            two_cnt += 1
        if 3 in cnts.values():
            three_cnt += 1
    return two_cnt * three_cnt

test_input = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
assert get_checksum(test_input) == 12
print(get_checksum(inputs))

## Part 2
def get_num_diff(s_1: str, s_2: str) -> int:
    diff = 0
    for l_1, l_2 in zip(s_1, s_2):
        if l_1 != l_2:
            diff += 1
    return diff

assert get_num_diff('abc', 'aac') == 1

def find_good_boxes(inputs: List[str]) -> Tuple[str, str]:
    for s_1 in inputs:
        for s_2 in inputs:
            if get_num_diff(s_1, s_2) == 1:
                return (s_1, s_2)

def get_common_letters(inputs: List[str]) -> str:
    good_boxes = find_good_boxes(inputs)
    box_1, box_2 = good_boxes[0], good_boxes[1]
    good_letters = ''.join([l_1 for l_1, l_2 in zip(box_1, box_2) if l_1 == l_2])
    return good_letters

assert get_common_letters(['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']) == 'fgij'
print(get_common_letters(inputs))
