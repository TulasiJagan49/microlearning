"""
This code is for solution to leetcode 977
"""

def three_sum(nums: list[int]) -> list[list[int]]:

    '''
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.
    
    DSA Pattern: Two Pointer Method.
    '''

    nums_length = len(nums)
    if nums_length < 3:
        return []
    
    nums.sort()
    results = []

    for i in range(nums_length - 2):

        if nums[i] > 0:
            break

        if i > 0 and nums[i] == nums[i-1]:
            continue

        left = i + 1
        right = nums_length - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                results.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while nums[left] == nums[left - 1] and left < right:
                    left += 1
                while nums[right] == nums[right + 1] and left < right:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return results

print(three_sum([-1,0,1,2,-1,-4]))
print(three_sum([0,0,0]))
