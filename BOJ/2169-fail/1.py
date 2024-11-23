import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dp = list(list(map(int, input().split())) for _ in range(n))

for i in range(1, m):
    dp[0][i] += dp[0][i - 1]

# 위에서 아래로만 갈 수 있기에 그렇게 진행
# 1번 idx 이후 행별로는 좌우 갚 비교하기
for i in range(1, n):
    ltr = dp[i][:]
    rtl = dp[i][:]

    # 왼쪽에서 오른쪽
    for j in range(m):
        if j == 0:
            ltr[j] += dp[i - 1][j]
        else:
            ltr[j] += max(dp[i - 1][j], ltr[j - 1])

    # 오른쪽에서 왼쪽
    for j in reversed(range(m)):
        if j == m - 1:
            rtl[j] += dp[i - 1][j]
        else:
            rtl[j] += max(dp[i - 1][j], rtl[j + 1])

    for j in range(m):
        dp[i][j] = max(ltr[j], rtl[j])

print(dp[-1][-1])
