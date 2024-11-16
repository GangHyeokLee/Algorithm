r1, c1, r2, c2 = map(int, input().split())

n = max(abs(r1), abs(c1), abs(r2), abs(c2))

# 전체 모눈종이의 너비 혹은 소용돌이의 너비
n = 2 * n + 1

def makeCyclone(n):
    sy, sx = n//2, n//2

    cycle = [[0] * n for _ in range(n)]
    cycle[sy][sx] = 1

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    d = 0
    l = 1
    number = 2

    while sy < n and sx < n:
        for i in range(l):
            sy = sy + dy[d]
            sx = sx + dx[d]

            if sy >= n or sx >= n:
                break

            cycle[sy][sx] = number
            number += 1
        d = (d + 1) % 4
        if d == 0 or d == 2:
            l += 1

    return cycle

cycle = makeCyclone(n)

r1 += n//2
r2 += n//2
c1 += n//2
c2 += n//2

for i in range(r1, r2+1):
    row = cycle[i]
    print(' '.join(map(str,row[c1:c2+1])))
