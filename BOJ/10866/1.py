from collections import deque
import sys

input = sys.stdin.readline

queue = deque()

n = int(input())
for _ in range(n):
  command = list(input().split())
  if command[0] == 'push_back':
    queue.append(command[1])
  elif command[0] == 'push_front':
    queue.appendleft(command[1])
  elif command[0] == 'front':
    print(queue[0] if len(queue) else -1)
  elif command[0] == 'back':
    print(queue[-1] if len(queue) else -1)
  elif command[0] == 'pop_front':
    print(queue.popleft() if len(queue) else -1)
  elif command[0] == 'pop_back':
    print(queue.pop() if len(queue) else -1)
  elif command[0] == 'size':
    print(len(queue))
  elif command[0] == 'empty':
    print(0 if len(queue) else 1)
  