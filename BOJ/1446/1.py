import sys

sys.setrecursionlimit(10 ** 6)

n, d = map(int, input().split())

# 거리 저장할 리스트 초기화
memo = [-1 for _ in range(d+1)]

# 도착지 기준 시작점과 거리 저장
road = {}
for _ in range(n):
  start, end, dist = map(int, input().split())
  
  # 고속도로 벗어나는 end는 생략
  if end > d:
    continue

  if end in road:
    road[end].append((dist, start))
  else:
    road[end] = [(dist, start)]
    

memo[0] = 0

# x만큼 가려면 얼마나 걸리는지 계산
def drive(x):
  # memo에서 안 구해졌을 경우
  if memo[x] == -1:
    # 혹시 지름길 도착지 있으면 그거 고려해서 다시 계산하기
    newMin = d
    if x in road:
      for dist, s in road[x]:
        # s까지 운전한 거리 + 지름길 길이 vs 이때까지 구한 min
        newMin = min(drive(s) + dist, newMin)
    # 새로 구한 거리 vs 바로 전칸에서 온 거리
    memo[x] = min(drive(x-1) + 1, newMin)
  return memo[x]

print(drive(d))