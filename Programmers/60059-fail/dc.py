def solution(key, lock):
    N= len(lock)
    M= len(key)
    
    # 자물쇠의 홈 부분을 찾기위해 lock을 확대하고, 패딩 추가
    expand_lock = [[0] * (N+2*(M-1)) for _ in range(N+2*(M-1))]
    
    # 확대된 lock의 가운데 기존 lock 배치
    for i in range(N):
        for j in range(N):
            expand_lock[i+M-1][j+M-1] = lock[i][j]
    
    #key를 회전시키는 함수
    def rotate(key):
        return [[key[M-1-j][i] for j in range(M)] for i in range(M)]
    
    #key가 lock에 맞는지 확인하는 함수
    def can_open(x, y, key):
        #lock의 모든 홈에 채워졌는 지 확인
        temp_lock = [row[:] for row in expand_lock]
        for i in range(M):
            for j in range(M):
                if key[i][j] == 1:
                    if temp_lock[x+i][y+j] == 1:
                        return False
                    temp_lock[x+i][y+j] = 1
    
        for i in range(N):
            for j in range(N):
                if temp_lock[i+M-1][j+M-1] == 0:
                    return False
        return True
    
    # 키를 회전/이동하면서 lock을 열 수 있는지 체크    
    for rotation in range(4):
        for x in range(N+M-1):
            for y in range(N+M-1):
                if can_open(x, y, key):
                    return True
        key = rotate(key)
    
    return False