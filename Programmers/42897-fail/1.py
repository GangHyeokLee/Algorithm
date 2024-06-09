def rob(money):
  dp = [0] * len(money)
  dp[0] = money[0]
  dp[1] = max(money[0], money[1])
  
  for i in range(2, len(money)):
    dp[i] = max(dp[i-2] + money[i], dp[i-1])
  
  return dp[-1]

def solution(money):
    # 점화식
    # dp[n] = max(dp[n-2] + money[n], dp[n-1])
    
    return max(rob(money[1:]), rob(money[:-1]))