def solution(arrows):
    answer = 0
    
    record = dict()
    record[(0,0)] = True
    cur = (0, 0)
    
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    
    # 엣지 방문기록 저장용, 0번은 0, 0
    visited = dict()
    
    for a in arrows:
        for _ in range(2):
            next = (cur[0] + dy[a], cur[1] + dx[a])
            
            # 처음 방문한 방향인데 이미 지나간 점에 접근할 때
            if (cur, next) not in visited and next in record:
                answer += 1
            
            visited[(next, cur)] = visited[(cur, next)] = True
            record[next] = True
            cur = next
    
    return answer