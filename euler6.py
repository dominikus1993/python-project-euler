def solve() -> int: 
    nums = range(1, 101)
    sum_of_square = sum(map(lambda x: x ** 2, nums))
    square_sum = sum(nums) ** 2
    return square_sum - sum_of_square