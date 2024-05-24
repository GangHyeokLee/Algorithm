from heapq import heappop, heappush

def solution(jobs):
    answer = 0
    time = 0
    next = False
    
    heap = []
    for j in jobs:
      heappush(heap, [j[1], j[0]])
    
    while heap:
      now = heappop(heap)
      
      tmp = []
      while now[1] > time and heap:
        tmp.append(now)
        now = heappop(heap)
      
      
      if not heap and now[1] > time:
        heappush(heap, now)
        time += 1
        next = True
      
      for t in tmp:
        heappush(heap, t)

        
      if next:
        next = False
        continue
      
      answer += time + now[0] - now[1]
      time += now[0]
    return answer // len(jobs)
  
  
# print(solution([[0, 3], [1, 9], [2, 6]]))
# print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]))
print(solution([[1,4],[7,9],[1000,3]]))