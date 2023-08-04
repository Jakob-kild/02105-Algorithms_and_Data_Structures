startVals = list(map(int, input().split()))
N = int(startVals[0])
W = int(startVals[1])
stones = list(map(int, input().split()))

def mergeSort(arr, i, j):
    if i < j:
        m = (i+j)//2
        mergeSort(arr, i, m)
        mergeSort(arr, m+1, j)
        merge(arr, i, m, j)
    return arr

def merge(arr, first, m, last):
    n1 = m - first + 1
    n2 = last - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[first + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = first  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[]
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[]
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

sortedStones = mergeSort(stones, 0, N-1)
res = 0
carry = 0
for stone in sortedStones:
    if (stone + carry) > W:
        break
    else:
        carry += stone
        res += 1
print(res)