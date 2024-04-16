# 못 풀었습니다.

# 어차피 집중국 끼면 덩어리끼리 합쳐짐 => 덩어리 사이 거리 긴 것부터 쳐내기
n = int(input())
k = int(input())
sensors = sorted(list(map(int, input().split())))

if k >= n:
  print(0)
else:
  diff = []
  for i in range(1, n):
    diff.append(sensors[i] - sensors[i-1])
    
  # 집중국이 커버해야할 최대 거리
  ans = sensors[-1] - sensors[0]

  diff.sort()
  for i in range(k-1):
    ans -= diff.pop()
    
  print(ans)