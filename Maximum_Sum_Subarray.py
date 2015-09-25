def Maximum_Sum_Subarray_On3(arr, n):
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

    
def Max_Subarray_Sum_brute(arr,n):	
    if (n == 1):
        return arr[0]
    m = n/2
    left_MSS = Max_Subarray_Sum(arr,m)
    right_MSS = Max_Subarray_Sum(arr+m,n-m)
    leftsum = INT_MIN, rightsum = INT_MIN, sum=0
    for i in range(m,n): #(int i=m;i < n; i++)
        sum += arr[i]
        rightsum = max(rightsum,sum)
    sum = 0
    for i in range ((m-1), 0, -1): #for(int i= (m-1);i >= 0; i--)
        sum += arr[i]
        leftsum = max(leftsum,sum)
    ans = max(left_MSS,right_MSS)
    return max(ans,leftsum+rightsum)


in_list = [-1, -1, -1, -1, 42]
Maximum_Sum_Subarray(in_list, len(in_list))
Max_Subarray_Sum(in_list, len(in_list))
