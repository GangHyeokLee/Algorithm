class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        sumDif = 0

        minV = 0
        maxV = 0
        for d in differences:
            sumDif += d
            minV = min(minV, sumDif)
            maxV = max(maxV, sumDif)


        start = lower - minV
        end = upper - maxV

        return end - start + 1 if end >= start else 0