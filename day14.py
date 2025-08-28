def count_substrings_with_k_distinct(s, k):
    n = len(s)
    result = 0
    
    # Generate all substrings
    for i in range(n):
        distinct = set()
        for j in range(i, n):
            distinct.add(s[j])
            if len(distinct) == k:
                result += 1
            elif len(distinct) > k:
                break
    return result

# Take input from user
s = input("Enter a string: ")
k = int(input("Enter the value of k: "))

print("Number of substrings with exactly", k, "distinct characters:", 
      count_substrings_with_k_distinct(s, k))