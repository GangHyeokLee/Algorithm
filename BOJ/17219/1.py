import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pwd = {}
for _ in range(n):
  a, b = input().split()
  pwd[a] = b
  
for _ in range(m):
  print(pwd[input().strip()])