'''
This code is for solution to leetcode 1 when the input array is sorted.
'''
def two_sum(nums: list, target: int)-> list[int]:

    '''
    Dsa Pattern: Two pointers
    '''

    start = 0
    end = len(nums) - 1

    while start < end:
        curr_sum = nums[start] + nums[end]

        if (curr_sum == target):
            return [start, end]
        
        if curr_sum < target:
            start += 1
        else:
            end -= 1
    
    return [-1, -1]

print(two_sum([2,7,11,15], 9))
