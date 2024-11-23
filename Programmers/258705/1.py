def solution(n, tops):
    upper = set()
    for idx, t in enumerate(tops):
        if t:
            upper.add((idx + 1) * 2 - 1)

    dp = [0] * (2 * n + 1)
    dp[0] = 1
    dp[1] = 3 if 1 in upper else 2

    for x in range(2, 2 * n + 1):
        dp[x] = (dp[x - 1] + dp[x - 2] + (dp[x - 1] if x in upper else 0)) % 10007

    return dp[-1] % 10007
