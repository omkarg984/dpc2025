def merge(arr1, arr2, m, n):
    def nextGap(gap):
        if gap <= 1:
            return 0
        return (gap // 2) + (gap % 2)

    gap = m + n
    while gap > 0:
        gap = nextGap(gap)
        i = 0
        while i + gap < m:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1
        j = gap - m if gap > m else 0
        while i < m and j < n:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1
        if j < n:
            k = j
            while k + gap < n:
                if arr2[k] > arr2[k + gap]:
                    arr2[k], arr2[k + gap] = arr2[k + gap], arr2[k]
                k += 1

arr1 = list(map(int, input("Enter sorted list 1 (space-separated): ").split()))
arr2 = list(map(int, input("Enter sorted list 2 (space-separated): ").split()))

merge(arr1, arr2, len(arr1), len(arr2))

print("After merging:")
print("arr1 =", arr1)
print("arr2 =", arr2)