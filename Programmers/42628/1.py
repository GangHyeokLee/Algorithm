from heapq import heappush, heappop

def solution(operations):
    answer = []
    
    maxHeap = []
    minHeap = []
    
    chk = dict()
    
    for oper in operations:
      o = oper.split()
      if o[0] == 'I':
        heappush(minHeap, int(o[1]))
        heappush(maxHeap, -int(o[1]))
        
        if int(o[1]) in chk:
          chk[int(o[1])] += 1
        else:
          chk[int(o[1])] = 1
        
      elif o[0] == 'D' and o[1] == '-1' and minHeap:
        min = heappop(minHeap)
        
        while chk[min] <= 0 and minHeap:
          min = heappop(minHeap)
        
        chk[min] -= 1
        
      elif o[0] == 'D' and o[1] == '1' and maxHeap:
        max = heappop(maxHeap)
        while chk[-max] <= 0 and maxHeap:
          max = heappop(maxHeap)
        chk[-max] -= 1

    if minHeap and maxHeap:
      min = heappop(minHeap)
      while chk[min] <= 0:
        min = heappop(minHeap)
      
      max = heappop(maxHeap)
      while chk[-max] <= 0:
        max = heappop(maxHeap)
      return [-max, min]
    else:
      return [0, 0]
      
  
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))