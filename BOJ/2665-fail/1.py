from heapq import heappush, heappop

n = int(input())

room = list(list(map(int, list(input()))) for _ in range(n))
cost = list([n*n] * n for _ in range(n))
cost[0][0] = 0

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

que = [(0, 0, 0)]

while que:
    count, y, x = heappop(que)

    if cost[y][x] < count:
        continue

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if 0 <= ny < n and 0 <= nx < n:
            if cost[ny][nx] > count + abs(room[ny][nx] - 1):    
                cost[ny][nx] = count + abs(room[ny][nx]-1)
                heappush(que, (cost[ny][nx], ny, nx))
print(cost[-1][-1])