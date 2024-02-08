from collections import deque

n, W, L = map(int, input().split())

trucks = deque(map(int, input().split()))

bridge = deque()

l = trucks[0]
bridge.append(trucks.popleft())

t = 1


while len(trucks):
  t += 1
  if len(bridge) < W and (l + trucks[0]) <= L:
    l += trucks[0]
    bridge.append(trucks.popleft())
  elif len(bridge) == W and (l + trucks[0] - bridge[0]) <= L:
    l += trucks[0]
    bridge.append(trucks.popleft())
  else:
    bridge.append(0)
  
  if len(bridge) > W:
    l -= bridge.popleft()

print(t + W)