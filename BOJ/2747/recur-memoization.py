fibo = [0] * 50

fibo[0] = 0
fibo[0] = 1

def fibonacci(n):
  if n==0:
    return 0
  if n==1:
    return 1
  
  if fibo[n] == 0:
    fibo[n] = fibonacci(n-1) + fibonacci(n-2)
  
  return fibo[n]

print(fibonacci(int(input())))