def solution(arrows):
    answer = 0
    start = 0
    
    record = set()
    record.add((0, 0))
    cur = (0, 0)
    
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    
    # 엣지 방문기록 저장용, 0번은 0, 0
    visited = [[True] * (len(arrows)+1) for _ in range(len(arrows) + 1)]
    
    for i in range(len(arrows)):
        next = (cur[0] + dy[arrows[i]], cur[1] + dx[arrows[i]])
        
        # 처음 방문한 방향인데 이미 지나간 점에 접근할 때
        if visited[start][i+1] and visited[i+1][start] and next in record:
          answer += 1
        
        visited[start][i+1] = visited[i+1][start] = False
        record.add(next)
        cur = next
        start = i+1
    
    return answer