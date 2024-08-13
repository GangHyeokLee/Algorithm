from heapq import heappop, heappush

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap = []
        minHeap = []

        for idx, c in enumerate(capital):
            heappush(maxHeap, (-profits[idx], c))

        for _ in range(k):
            while minHeap and minHeap[0][0] <= w:
                c, p = heappop(minHeap)
                heappush(maxHeap,(p, c))

            while maxHeap and maxHeap[0][1] > w:
                p, c = heappop(maxHeap)
                heappush(minHeap, (c, p))
            
            if not maxHeap:
                break
            
            pro, cap = heappop(maxHeap)

            w -= pro
        return w