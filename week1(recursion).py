
n = input()
array = list(map(int, input().split()))


def peak1(array, n):
    if array[0] >= array[1]:
        return 0
    for i in range(n-2):
        if array[i-1] <= array[i] >= array[i+1]:
            return i
    if array[n-2] <= array[n-1]:
        return n-1

def peak2(array, n):
    max = 0
    for i in range(n):
        if array[i] > array[max]:
            max = i
    return max

def peak3(array, i, j):
    m = (i+j)//2
    if array[m] >= neighbors(array, m, "left") and array[m] >= neighbors(array, m, "right"):
        return m
    elif array[m-1] > array[m]:
        return peak3(array, i, m-1)
    elif array[m] < array[m+1]:
        return peak3(array, m+1, j)

def neighbors(array, i, orintation):
    if orintation == "left":
        if i == 0:
            return 0
        else:
            return array[i-1]
    elif orintation == "right":
        if i == len(array)-1:
            return 0
        else:
            return array[i+1]

print(peak3(array, 0, int(n)))
