def solution(info, n, m):
    from collections import deque

    # dp[a][b] = True : A 도둑 흔적 a, B 도둑 흔적 b 상태가 가능한 경우
    dp = [[False] * m for _ in range(n)]
    dp[0][0] = True  # 시작 상태

    for a_trace, b_trace in info:
        new_dp = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not dp[i][j]:
                    continue

                # A 도둑이 이 물건을 훔치는 경우
                if i + a_trace < n:
                    new_dp[i + a_trace][j] = True

                # B 도둑이 이 물건을 훔치는 경우
                if j + b_trace < m:
                    new_dp[i][j + b_trace] = True

        dp = new_dp  # 갱신

    # 가능한 상태 중 A 흔적의 최소값 찾기
    for i in range(n):
        for j in range(m):
            if dp[i][j]:
                return i  # A 도둑 흔적 최소

    return -1  # 가능한 상태 없음
