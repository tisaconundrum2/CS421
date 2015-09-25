def Maximum_Sum_Subarray(arr, n):
    ans = float('-inf')
    for sub_array_size in range(1, n + 1):
        for start_index in range(0, n):
            if start_index + sub_array_size > n:
                break
            sum = 0;
            for i in range(start_index, start_index + sub_array_size):
                sum += arr[i]
                ans = max(ans, sum)
    return ans


in_list = [-1, -1, -1, -1, 42]
Maximum_Sum_Subarray(in_list, len(in_list))
