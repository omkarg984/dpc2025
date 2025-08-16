def find_missing_number(arr):
    n = len(arr) + 1  
    total_sum = n * (n + 1) // 2
    return total_sum - sum(arr)

arr = list(map(int, input("Enter the array elements separated by space: ").split()))

print("Missing number is:", find_missing_number(arr))