case = 0

while True:
  L, P, V = map(int, input().split())
  if L==0 and P == 0 and V == 0:
    break
  case += 1

  ans = (V // P) * L + min(V % P, L)

  print('Case ' + str(case) + ': ' + str(ans))


