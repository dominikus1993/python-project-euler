import math
from typing import List

def is_divisable_by_all_numbers (number: int, nums: List[int]) -> List[int]:
    return len(list(filter(lambda x: number % x != 0, nums))) == 0



def solve() -> int:
    nums = range(2, 21)
    i = 232792100
    while True:
        if is_divisable_by_all_numbers(i, nums):
            break
        else:
            i = i + 1
    return i
