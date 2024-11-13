from collections import defaultdict

n = int(input())

work = list(list(map(int, input().split())) for _ in range(n))
time = [0] * (n+1)
graph = defaultdict(list)
queue = []
visited = [0] * (n+1)
done = [0] * (n+1)

for idx, w in enumerate(work):
    graph[idx+1] = []
    time[idx+1] = w[0]

    if w[1] == 0:
        queue.append(idx+1)
    else:
        visited[idx+1] = w[1]

    for i in range(w[1]):
        graph[w[i+2]].append(idx+1)


idx = 0

for q in queue:
    done[q] = time[q]

while idx < len(queue):
    now = queue[idx]
    idx += 1

    for next in graph[now]:
        visited[next]-=1
        done[next] = max(done[next], done[now] + time[next])
        if visited[next] == 0:
            queue.append(next)

print(max(done))