def get_permutations(s):
    if len(s) == 1:
        return [s]
    
    permutations = []
    
    for i in range(len(s)):
        char = s[i]
        remaining = s[:i] + s[i+1:]
        
        for perm in get_permutations(remaining):
            new_perm = char + perm
            if new_perm not in permutations:
                permutations.append(new_perm)
    
    return permutations

s = input("Enter a string: ")
result = get_permutations(s)
print("All unique permutations:")
print(result)