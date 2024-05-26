class Solution:
    def putMarbles(self, weights, k: int) -> int:
        endStart = []
        for i in range(len(weights) -1):
            endStart.append(weights[i] + weights[i+1])
        endStart.sort()
        
        ans = 0
        for j in range(k-1):
            ans += endStart[-1 -j] - endStart[j]
        
        return ans