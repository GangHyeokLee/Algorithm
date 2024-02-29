from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

queue = deque()


for _ in range(n):
  command = list(input().split())
  
  if len(command) > 1:
    queue.append(command[1])
  elif command[0] == 'front':
    print(queue[0] if len(queue) else -1)
  elif command[0] == 'back':
    print(queue[-1] if len(queue) else -1)
  elif command[0] == 'pop':
    print(queue.popleft() if len(queue) else -1)
  elif command[0] == 'size':
    print(len(queue))
  elif command[0] == 'empty':
    print(0 if len(queue) else 1)
    
    
