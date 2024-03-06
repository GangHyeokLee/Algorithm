fibo = [[0, 1, 0], [1, 0, 1]]
def fibonacci(n):  
  if n == 0:
    return fibo[0]
  if n == 1:
    return fibo[1]
  
  if len(fibo) >= n + 1:
    return fibo[n]
  
  n1 = fibonacci(n-1)
  n2 = fibonacci(n-2)
  
  fibo.append([n1[0]+n2[0], n1[1]+n2[1], n1[2]+n2[2]])
  return fibo[n]

t = int(input())

for _ in range(t):
  ans = fibonacci(int(input()))
  print(ans[1], ans[2])