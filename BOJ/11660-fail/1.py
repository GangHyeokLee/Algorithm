import sys
input = sys.stdin.readline

n, m = map(int, input().split())

table = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n + 1):
  row = list(map(int, input().split()))
  for j in range(1, n+1):
    # 위 아래 둘이 합친 값 더하기, 대각선은 중복이라서 빼고
    table[i][j] = table[i-1][j] + table[i][j-1] - table[i-1][j-1] + row[j-1]

for _ in range(m):
  y1, x1, y2, x2 = map(int, input().split())
  # table y2x2는 1,1, y2, x2 그래서 위 아래 덩어리 잘라내고, x1-1, y1-1 만큼은 중복이라서 다시 더해주기
  print(table[y2][x2] - table[y1-1][x2] - table[y2][x1-1] + table[y1-1][x1-1])