def capitalize_first_last(s: str) -> str:
        # Your code goes here
        s_arr = s.split(' ')
        for idx, word in enumerate(s_arr):
            if len(word) > 1:
                s_arr[idx] = f"{word[0].upper()}{word[1:-1]}{word[-1].upper()}"
            else:
                s_arr[idx] = word.upper()
        
        return " ".join(s_arr)

print(capitalize_first_last("take u forward is awesome"))