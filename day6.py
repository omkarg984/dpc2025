def find_zero_sum_subarrays(arr):
    result = []
    n = len(arr)

    for start in range(n):
        total = 0
        for end in range(start, n):
            total += arr[end]
            if total == 0:
                result.append((start, end))
    return result

user_input = input("Enter numbers separated by commas: ")
arr = list(map(int, user_input.split(",")))

print("Input array:", arr)
print("Subarrays with zero sum:", find_zero_sum_subarrays(arr))