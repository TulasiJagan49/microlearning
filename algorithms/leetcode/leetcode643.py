"""
This code is for solution to leetcode 643
"""

def maximum_average_subarray(nums: list, k: int):
    '''
    Question Description
    You are given an integer array nums consisting of n elements, and an integer k.
    Find a contiguous subarray whose length is equal to k that has the maximum
    average value and return this value. Any answer with a calculation error less
    than 10-5 will be accepted.
    
    DSA Pattern: Sliding Window 
    '''
    window_sum = 0
    window_start = 0
    max_sum = float('-inf')

    for idx, num in enumerate(nums, start = 1):

        window_sum += num

        if idx >= k:

            max_sum = max(window_sum, max_sum)

            window_sum -= nums[window_start]

            window_start += 1

    return max_sum / k

print(maximum_average_subarray([1,12,-5,-6,50,3], 4))
