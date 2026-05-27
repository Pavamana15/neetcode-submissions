import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        

        meeting_times = []

        for start, end, pro in zip(startTime, endTime, profit):
            meeting_times.append([start, end, pro])

        meeting_times.sort(key=lambda x: x[0])

        # Extract start times for binary search
        starts = [m[0] for m in meeting_times]

        n = len(meeting_times)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            start, end, pro = meeting_times[i]
            
            # Find next non-overlapping meeting
            j = bisect.bisect_left(starts, end)
            
            dp[i] = max(dp[i + 1], pro + dp[j])

        return dp[0]


        