import sys

input = sys.stdin.readline

n = int(input())

emp = {}

for _ in range(n):
  name, inout = input().split()
  
  if inout == 'enter':
    emp[name] = True
  else:
    emp[name] = False
    
enter = []
for k, v in emp.items():
  if v:
    enter.append(k)
    
enter.sort()
enter.reverse()
for i in enter:
  print(i)