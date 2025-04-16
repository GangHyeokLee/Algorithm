from collections import deque

n, m = map(int, input().split())

que = deque([i for i in range(1, n + 1)])
targets = list(map(int, input().split()))

count = 0

for i, num in enumerate(targets):
    idx = que.index(num)

    if idx <= len(que) // 2:
        for i in range(idx):
            que.append(que.popleft())
            count += 1
    else:
        for i in range(len(que) - idx):
            que.appendleft(que.pop())
            count += 1
    que.popleft()
print(count)
