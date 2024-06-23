from collections import deque

class Solution:
    def continuousSubarrays(self, nums) -> int:
        min_deque = deque()
        max_deque = deque()
        start = 0
        count = 0

        for i in range(len(nums)):
            while min_deque and nums[i] < nums[min_deque[-1]]:
                min_deque.pop()
            while max_deque and nums[i] > nums[max_deque[-1]]:
                max_deque.pop()
            
            min_deque.append(i)
            max_deque.append(i)
            
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                if min_deque[0] < max_deque[0]:
                    start = min_deque.popleft() + 1
                else:
                    start = max_deque.popleft() + 1
            
            count += i - start + 1
        
        return count