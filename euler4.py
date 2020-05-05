def is_palindrome(num: int) -> bool: 
    str_num = str(num)
    reversed_str = str_num[::-1]
    return str_num == reversed_str

def generate(): 
    for x in range(1, 1001):
        for y in range(1, 1001):
            yield x * y

def solve():
    return max(filter(lambda y: is_palindrome(y), generate()))