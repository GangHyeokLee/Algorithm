from collections import defaultdict

n = int(input())
parent = list(map(int, input().split()))

company = defaultdict(list)

# Correct loop starting from 1 to properly handle root node 0
for i in range(1, n):
    company[parent[i]].append(i)

child = [0] * n

# Calculate children count correctly
for i in range(n-1, 0, -1):
    child[parent[i]] += child[i] + 1

que = [(0, 0)]

idx = 0

while idx < len(que):
    now, time = que[idx]
    idx += 1

    # Sort children by the number of subordinates
    company[now].sort(key=lambda x: -child[x])
  
    # Append children to queue with the calculated time
    for i, v in enumerate(company[now]):
        que.append((v, time + 1 + i))

# Output the maximum propagation time
print(max(que, key=lambda x: x[1])[1])
