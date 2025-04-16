dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for _ in range(int(input())):
    m, n, k = map(int, input().split())

    plain = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        plain[y][x] = 1

    ans = 0
    for i in range(n):
        for j in range(m):
            if plain[i][j] == 1:
                ans += 1
                que = [(i, j)]
                plain[i][j] = 0
                idx = 0
                while idx < len(que):
                    y, x = que[idx]
                    idx += 1
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]

                        if 0 <= ny < n and 0 <= nx < m and plain[ny][nx] == 1:
                            plain[ny][nx] = 0
                            que.append((ny, nx))
    print(ans)
