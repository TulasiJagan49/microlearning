def longest_semi_repetitive_substring(s: str) -> int:

    str_length = len(s)
    if str_length <= 2: return str_length

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