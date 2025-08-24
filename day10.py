def groupAnagrams(strs):
    groups = {}

    for word in strs:
        key = "".join(sorted(word))  # sort letters
        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    return list(groups.values())


# --- Main program ---
# Take input from user
user_input = input("Enter words separated by spaces: ")

# Split input into list of words
words = user_input.split()

# Call the function
result = groupAnagrams(words)

# Print result
print("Grouped Anagrams:")
print(result)