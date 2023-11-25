def merge(arr, l, m ,r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    # create new arr on the left
    for i in range(n1):
        L[i] = arr[l + i]
    # create new arr on the right
    for i in range(n2):
        R[i] = arr[m + 1 + i]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        mid = l + (r - l) // 2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)
        merge(arr, l, mid, r)


arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is: ")
for i in range(n):
    print("%d" % arr[i], end=" ")