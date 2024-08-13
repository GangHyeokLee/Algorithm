from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pc = defaultdict(list)

        for idx, c in enumerate(capital):
            heappush(pc[c], -profits[idx])

        for i in range(k):
            cap = w
            maxPro = 0
            maxCap = cap
            while cap >= 0:
                if pc[cap]:
                    if maxPro < -min(pc[cap]):
                        maxPro = -min(pc[cap])
                        maxCap = cap
                cap -= 1

            # print(maxCap)
            
            if cap == -1 and maxPro == 0:
                break

            # print(i, w, maxCap)
            w += -heappop(pc[maxCap])
            
        
        return w