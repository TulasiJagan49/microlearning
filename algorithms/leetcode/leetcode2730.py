"""
This code is for solution to leetcode 2730
"""

def longest_semi_repetitive_substring(s: str) -> int:

    '''
    You are given a digit string s that consists of digits from 0 
    to 9.

    A string is called semi-repetitive if there is at most one 
    adjacent pair of the same digit. For example, "0010", 
    "002020", "0123", "2002", and "54944" are semi-repetitive 
    while the following are not: "00101022" (adjacent same digit 
    pairs are 00 and 22), and "1101234883" (adjacent same digit 
    pairs are 11 and 88).

    Return the length of the longest semi-repetitive substring of 
    s.

    DSA Pattern: Sliding Window with two pointer
    '''

    str_length = len(s)
    if str_length <= 2:
        return str_length

    max_length = 0
    left = 0
    adjacent_pair_count = 0
    last_pair_index = 0

    for right in range(1, str_length):
       
        if s[right] == s[right - 1]:
            adjacent_pair_count += 1

            if adjacent_pair_count > 1:
                left = last_pair_index
           
            last_pair_index = right
       
        max_length = max(max_length, right - left + 1)

    return max(max_length, 1) if str_length > 0 else 0

print(longest_semi_repetitive_substring("52233"))
