n, c = map(int, input().split())
home = [int(input()) for _ in range(n)]

home.sort()

# 거리 기준으로 공유기 설치할 수 있는 개수 계산하기
start = 0
end = max(home) - min(home) #가장 멀리 설치하기

while start <= end:
  mid = (start + end) // 2
  
  located = -1
  total = 0
  #공유기 개수 계산
  for i in home:
    #첫 시작이거나 새로 설치할 곳이 mid 이상일 때
    if located < 0 or i - located >= mid: 
      total += 1
      located = i
    else:
      continue
  
  # 설치할 수 있는 공유기가 더 많음
  if total >= c:
    start = mid + 1
  else:
    end = mid - 1
    
print(end)