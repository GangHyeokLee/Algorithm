def solution(arr):
    answer = -1
    
    nums = []
    ops = []
    
    for a in arr:
        if a == '+' or a == '-':
            ops.append(a)
        else:
            nums.append(int(a))
            
    n = len(nums)
    
    max_dp = [[-2000] * n for _ in range(n)]
    min_dp = [[2000] * n for _ in range(n)]
    
    for length in range(n):
        for i in range(n-length):
            j = i + length
            if i == j:
                max_dp[i][j] = min_dp[i][j] = nums[i]
                continue
            for mid in range(i, j):
                if ops[mid] == '+':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][mid] + max_dp[mid+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][mid] + min_dp[mid+1][j])
                elif ops[mid] == '-':
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][mid] - max_dp[mid+1][j])
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][mid] - min_dp[mid+1][j])
    
    return max_dp[0][-1]