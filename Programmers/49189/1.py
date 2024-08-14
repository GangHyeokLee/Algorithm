from collections import defaultdict

def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    que = []
    idx = 0
    que.append((1, 0))
    visited = [True] * (n+1)
    visited[1] = False
    while idx < len(que):
        now, count = que[idx]
        idx += 1
        
        for next in graph[now]:
            if visited[next]:
                visited[next] = False
                que.append((next, count+1))
                
    max = que[-1][1]
    
    for idx, length in que:
        if max == length:
            answer+=1
    
    return answer