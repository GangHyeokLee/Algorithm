def solution(n):
    
    row = [False] * n
    diagonal1 = [False] * (2 * n - 1)
    diagonal2 = [False] * (2 * n - 1)
    
    def dfs(y):
        if y == n:
            return 1
        answer = 0
        for x in range(n):
            if not row[x] and not diagonal1[y + x] and not diagonal2[y - x + n - 1]:
                row[x] = diagonal1[y+x] = diagonal2[y-x+n-1] = True
                answer += dfs(y+1)
                row[x] = diagonal1[y+x] = diagonal2[y-x+n-1] = False
        return answer
    
    return dfs(0)