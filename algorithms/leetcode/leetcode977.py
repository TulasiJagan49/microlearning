"""
This code is for solution to leetcode 977
"""

def sorted_sqaures(nums: list[int]) -> list[int]:
    '''
    Given an integer array nums sorted in non-decreasing order, return 
    an array of the squares of each number sorted in non-decreasing 
    order.

    DSA Pattern: Two pointers
    '''

    nums_length = len(nums)

    results = [0] * nums_length

    start = 0
    end = nums_length - 1
    idx = nums_length - 1

    while start <= end:

        square_at_start = nums[start] * nums[start]
        square_at_end = nums[end] * nums[end]

        if square_at_start > square_at_end:
            results[idx] = square_at_start
            start += 1
        else:
            results[idx] = square_at_end
            end -= 1

        idx -= 1

    return results

print(sorted_sqaures([-4,-1,0,3,10]))
