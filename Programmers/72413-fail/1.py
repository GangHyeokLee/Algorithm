def solution(n, s, a, b, fares):
    answer = 0
    
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n+1):
        dist[i][i] = 0
        
    for i, j, k in fares:
        dist[i][j] = k
        dist[j][i] = k
        
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    ans = [0] * (n + 1)
    
    for i in range(n + 1):
        ans[i] = dist[s][i] + dist[a][i] + dist[b][i]
    
    return min(ans)