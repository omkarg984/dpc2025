def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:  # closing bracket
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:  # opening bracket
            stack.append(char)

    return not stack


# ---- Main Program ----
s = input("Enter a string with brackets: ")
print("True" if isValid(s) else "False")