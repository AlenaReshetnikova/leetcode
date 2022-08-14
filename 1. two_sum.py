# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return
# indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
# Constraints:
#
# 2 <= nums.length <= 10**4
# -10**9 <= nums[i] <= 10**9
# -10**9 <= target <= 10**9
# Only one valid answer exists.
#
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
import time
from random import randint


def two_sum_1(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j, num in enumerate(nums[i+1:]):
            if nums[i] + num == target:
                return [nums.index(nums[i]), j+i+1]


def two_sum_2(nums: list, target: int) -> list:
    hash_table = {}
    for ind, value in enumerate(nums):
        if value not in hash_table:
            hash_table[target - value] = ind
        else:
            ind_1 = hash_table[value]
            return [ind_1, ind]


def out_ok_error(first, second):
    if isinstance(second, list) or isinstance(second, tuple):
        first = sorted(first)
        second = sorted(second)
    if first == second or second is None:
        return "\033[32m{}\033[0m".format("OK")
    else:
        return "\033[31m{}\033[0m".format("ERROR")



def time_in_work(time_s, time_end):
    return "\033[34m{}\033[0m".format(round(time_end - time_s, 4))


def execute(func, test):
    start = time.time()
    result = func(*test[0])
    end = time.time()
    print(f"{time_in_work(start, end)} sec and it is {out_ok_error(result, test[1])} {func.__name__} with numbers "
          f"{test[0][0] if len(test[0][0]) < 10 else test[0][0][:10]} and target {test[0][1]}, "
          f"need {test[1]}, but we get {result}")


tests = [
    [([2, 7, 11, 15], 9), [0, 1]],
    [([3, 2, 4], 6), [1, 2]],
    [([3, 3], 6), [0, 1]],
    [([randint(-10, 10) for _ in range(10)], randint(-10, 10)), None],
    [([randint(-100, 100) for _ in range(1000)], randint(-100, 100)), None],
    [([randint(-1000000, 1000000) for _ in range(1000000)], randint(-100000, 100000)), None],
    [([i for i in range(10000)], 9999+9998), None],
]

for test in tests:
    execute(two_sum_2, test)
    execute(two_sum_1, test)
    print()
