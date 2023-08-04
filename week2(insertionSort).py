startVals = list(map(int, input().split()))
N = int(startVals[0])
W = int(startVals[1])
stones = list(map(int, input().split()))

def insertionSort(array, n):
    for i in range(1, n):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array = swap(array, j, j-1)
            j -= 1
    return array

def swap(arr, i, j):
    swapVal = arr[j]
    arr[j] = arr[i]
    arr[i] = swapVal
    return arr

sortedStones = insertionSort(stones, N)
res = 0
carry = 0
for stone in sortedStones:
    if (stone + carry) > W:
        break
    else:
        carry += stone
        res += 1
print(res)