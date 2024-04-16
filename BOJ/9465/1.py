import sys
input = sys.stdin.readline

for _ in range(int(input())):
  n = int(input())
  sti = [list(map(int, input().split())), list(map(int, input().split()))]
  
  memo = [[0] * n for _ in range(2)]
  for i in range(1, n):
    # 두 칸 전에 있는 스티커 위 아래
    i02 = sti[0][i-2] if i > 1 else 0
    i12 = sti[1][i-2] if i > 1 else 0
    i2 = max(i02, i12)
    
    
    
    n2 = 0
    # n-2번째 칸 + n중에 큰 값 떼기 vs 
    
    n02 = i2 + sti[0][i]
    n12 = i2 + sti[1][i]
    
    n01 = sti[1][i-1] + sti[0][i]
    n11 = sti[0][i-1] + sti[1][i]
    
    sti[0][i] = max(n01, n02)
    sti[1][i] = max(n11, n12)
    
  print(max(max(sti[0]), max(sti[1])))