def lengthOfLongestSubstring(s: str) -> tuple:
    char_set = set()
    left = 0
    max_length = 0
    start_index = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        
        if (right - left + 1) > max_length:
            max_length = right - left + 1
            start_index = left

    return max_length, s[start_index:start_index + max_length]


# Take input from user
s = input("Enter a string: ")

length, substring = lengthOfLongestSubstring(s)
print("Length of longest substring without repeating characters:", length)
print("Longest substring:", substring)