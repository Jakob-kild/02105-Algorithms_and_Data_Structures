def max_subarray_sum(arr):
    def helper(start, end):
        if start == end:
            return arr[start]

        mid = (start + end) // 2

        left_max = helper(start, mid)
        right_max = helper(mid + 1, end)

        # Calculate the maximum sum that includes the middle element
        left_sum = float('-inf')
        current_sum = 0
        for i in range(mid, start - 1, -1):
            current_sum += arr[i]
            left_sum = max(left_sum, current_sum)

        right_sum = float('-inf')
        current_sum = 0
        for i in range(mid + 1, end + 1):
            current_sum += arr[i]
            right_sum = max(right_sum, current_sum)

        return max(left_max, right_max, left_sum + right_sum)

    return helper(0, len(arr) - 1)


# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Output the result
print(max_subarray_sum(arr))