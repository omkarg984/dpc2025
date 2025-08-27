def longest_palindrome(s: str) -> str:
    if not s or len(s) < 1:
        return ""

    start, end = 0, 0

    def expand_around_center(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(len(s)):
        len1 = expand_around_center(i, i)      # Odd length palindrome
        len2 = expand_around_center(i, i + 1)  # Even length palindrome
        max_len = max(len1, len2)

        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]


# Taking input from user
user_input = input("Enter a string: ")
print("Longest Palindromic Substring:", longest_palindrome(user_input))