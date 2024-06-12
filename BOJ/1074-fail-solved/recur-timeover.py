def solve(n, x, y):
  global result
  global find
  if find:
    return 
  if n==2:
    if x == X and y == Y:
      find = True
      print(result)
      return
    result += 1
    if x == X and y + 1 == Y:
      find = True
      print(result)
      return
    result += 1
    if x + 1 == X and y == Y:
      find = True
      print(result)
      return
    result += 1
    if x + 1 == X and y + 1 == Y:
      find = True
      print(result)
      return
    result += 1
    return
  solve(n/2, x, y)
  solve(n/2, x, y+n/2)
  solve(n/2, x+n/2, y)
  solve(n/2, x+n/2, y+n/2)

result = 0
find = False
N, X, Y = map(int, input().split())
solve(2 ** N, 0, 0)