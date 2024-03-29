a1, a0 = map(int, input().split())

c = int(input())

n0 = int(input())

fn = a1 * n0 + a0
gn = n0 * c

# n0일 때도 크고, 직선의 기울기도 더 크기
if fn <= gn and c >= a1:
  print(1)
else:
  print(0)