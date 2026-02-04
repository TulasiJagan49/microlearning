"""
This code is for solution to leetcode 904
"""

def total_fruit(fruits: list[int]) -> int:
    '''
    DSA Pattern: Sliding Window two pointer
    '''

    max_length = 0
    last = -1
    second_last = -1
    curr_length = 0
    last_count = 0

    for f in fruits:
        if f == last or f == second_last:
            curr_length += 1
        else:
            curr_length = last_count + 1
        
        if f == last:
            last_count += 1
        else:
            last_count = 1
            second_last, last = last, f
        
        max_length = max(max_length, curr_length)

    return max_length

print(total_fruit([1,2,3,2,2]))
