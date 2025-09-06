from collections import deque

def sliding_window_maximum(arr, k):
    n = len(arr)
    if n * k == 0:
        return []
    if k == 1:
        return arr

    dq = deque()
    result = []

    for i in range(n):
        if dq and dq[0] == i - k:
            dq.popleft()
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result

arr = list(map(int, input().split()))
k = int(input())
print(sliding_window_maximum(arr, k))