from collections import deque


def orderlyQueue(s: str, k: int) -> str:
  if k > 1:
    tmp = list(s)
    tmp.sort()
    return "".join(tmp)
  else:
    rotate = []
    s = deque(s)
    
    rotate.append("".join(s))
    for i in range(len(s)):
      s.append(s.popleft())
      rotate.append("".join(s))
    
    rotate.sort()
    return rotate[0]
        
        
print(orderlyQueue("cba", 1))
print(orderlyQueue("baaca", 3))
