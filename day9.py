def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for s in strs[1:]:
        while s[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

words = input("Enter words separated by spaces: ").split()

print("Longest Common Prefix:", longestCommonPrefix(words))