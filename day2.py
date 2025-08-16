def find_missing_number(arr):
    n = len(arr) + 1  # total numbers including the missing one
    total_sum = n * (n + 1) // 2  # sum of first n natural numbers
    return total_sum - sum(arr)

# Accept array input from user
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

print("Missing number is:", find_missing_number(arr))