r1, c1, r2, c2 = map(int, input().split())

n = max(abs(r1), abs(c1), abs(r2), abs(c2))

def cal_start(n):
    if n == 0:
        return 1
    return 4 * n * (n - 1) + 2

def cal_number(i, j):
    n = max(abs(i), abs(j))
    start_num = cal_start(n)
    if n == 0:
        return 1
    sy, sx = n-1, n

    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    d = 0

    turningPoint = {(-n, n), (-n, -n), (n, -n)}

    while (dy, dx) != (n, n+1):
        if sy == i and sx == j:
            return start_num

        if (sy, sx) in turningPoint:
            d = (d+1)%4

        sy += dy[d]
        sx += dx[d]
        start_num += 1



ans = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]
maxLen = 0
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        ans[abs(i - r1)][abs(j - c1)] = cal_number(i, j)
        maxLen = max(len(str(ans[abs(i - r1)][abs(j - c1)])), maxLen)

for line in ans:
    tmp = ""
    for l in line:
        for _ in range(maxLen - len(str(l))):
            tmp += " "
        tmp += str(l) + " "
    print(tmp[:-1])