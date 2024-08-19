class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        ans = 0
        jobs = []

        for i, s in enumerate(startTime):
            jobs.append((s, endTime[i], profit[i]))
        
        jobs.sort()

        print(jobs)

        dp = [0] * len(profit)
        dp[-1] = jobs[-1]

        for i in range(len(profit)-2, -1, -1):
            s, e, p = jobs[i]
            
            start = i+1
            end = len(dp)
            while start < end:
                mid = (start + end) // 2
                if jobs[mid][0] >= e:
                  end = mid
                else:
                  start = mid + 1

            if start < len(dp):
                dp[i] = max(dp[i+1], (s, dp[start][1], p + dp[start][2]), key=lambda x: x[2])
            else:
                dp[i] = max(dp[i+1], jobs[i], key=lambda x: x[2])
            
        return max(dp, key=lambda x: x[2])[2]