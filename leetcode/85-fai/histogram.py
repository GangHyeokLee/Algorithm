from collections import defaultdict

class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        
        heights = [0] * (c+1)
        
        ans = 0
        for row in matrix:
            for j in range(c):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            stack = []
            for j in range(c+1):
                while stack and heights[j] < heights[stack[-1]]:
                    last = stack.pop()
                    height = heights[last]
                    width = j - 1 - (stack[-1] if stack else -1)
                    ans = max(ans, height * width)
                stack.append(j)
        return ans
