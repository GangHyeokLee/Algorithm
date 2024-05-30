dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def rotate90(arr, length):    
    for i in range(len(arr)):
        y, x = arr[i]
        arr[i] = (x, length - y - 1)
    arr.sort()
            

def bfs(i, j, chk, limit, visited, board):
    queue = [(i, j)]
    idx = 0
    visited[i][j] = False
    
    while idx < len(queue):
        y, x = queue[idx]
        idx += 1
        
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            
            if 0 <= ny < limit and 0 <= nx < limit and board[ny][nx] == chk and visited[ny][nx]:
                visited[ny][nx] = False
                queue.append((ny, nx))
    queue.sort()
    return queue
            

def solution(game_board, table):
    answer = 0
    
    limit = len(game_board)
    
    visited_game = [[True] * limit for _ in range(limit)]
    visited_table = [[True] * limit for _ in range(limit)]
    
    game = [[] for _ in range(limit * limit + 1)]
    blocks = [[] for _ in range(limit * limit + 1)]
    
    
    for i in range(limit):
        for j in range(limit):
            if game_board[i][j] == 0 and visited_game[i][j]:
                tmp = bfs(i, j, 0, limit, visited_game, game_board)
                game[len(tmp)].append(tmp)
                
            if table[i][j] == 1 and visited_table[i][j]:
                tmp = bfs(i, j, 1, limit, visited_table, table)
                blocks[len(tmp)].append(tmp)      
            
    for i in range(limit * limit + 1):
        # 크기가 i인 빈 칸과 조각이 있을 때
        if game[i] and blocks[i]:
            for g in game[i]: # 크기가 i인 조각 여러 개 중 하나
                for j in range(len(blocks[i])): # 크기가 같은 조각 전체와 비교하기
                    b = blocks[i][j]
                    # 한 번 사용한 조각은 날릴 것.
                    if b:
                        for t in range(4): # 4번 회전 하는 동안 일치 여부 확인
                            found = True
                            # 평행 이동 거리 기준
                            dy = g[0][0] - b[0][0]
                            dx = g[0][1] - b[0][1]

                            for s in range(i):
                                # 한 칸이라도 평행이동 거리 다르면 정지
                                if dy != g[s][0] - b[s][0] or dx != g[s][1] - b[s][1]:
                                    found = False
                                    rotate90(b, limit)
                                    break
                            if found:
                                break

                        # 일치하는 조각 찾으면 해당 조각 빈 칸 처리
                        if found:
                            blocks[i][j] = []
                            answer += i
                            break
                            
    
    return answer