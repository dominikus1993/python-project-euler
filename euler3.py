import math
from typing import List

def find_factor(number: int) -> List[int]:
    upperBound = int(math.sqrt(number)) + 1
    return [x for x in range(2, upperBound) if number % x == 0]


def is_prime(number: int) -> bool:
    return len(find_factor(number)) == 0


def solve(number: int) -> bool:
    upperBound = int(math.sqrt(number)) + 1
    list = range(2, upperBound)
    return max(filter(lambda x: is_prime(x), filter(lambda y: number % y == 0, list)))
