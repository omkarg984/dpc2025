def first_element_to_repeat_k_times(arr, k):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    for num in arr:
        if freq[num] == k:
            return num
    return -1
print("Enter a list of integers separated by spaces : ",end=" ")
arr = list(map(int, input().split()))
print(" k = ",end=" ")
k = int(input())
print(f"The first element repeated {k} time(s) in the list is : ",end=" ")
result = first_element_to_repeat_k_times(arr, k)
print(result)