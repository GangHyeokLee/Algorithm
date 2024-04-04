from collections import defaultdict

for _ in range(int(input())):
  wear = defaultdict(int) # 의상 타입별 개수 저장할 공간
  for _ in range(int(input())):
    _, t = input().split()
    wear[t] += 1
  ans = 1
  for v in wear.values():
    ans *= (v + 1) #안 입는 경우 + 나머지 경우의 수 전부 곱하기
  
  print(ans-1) # 아무것도 안 입는 경우 1 빼기