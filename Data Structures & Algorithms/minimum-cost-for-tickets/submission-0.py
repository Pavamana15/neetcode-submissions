class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]* 367


        def next_greater( x):
            left = 0
            right = len(days) - 1
            answer = None

            while left <= right:
                mid = (left + right) // 2

                if days[mid] >= x:
                    answer = days[mid]
                    right = mid - 1
                else:
                    left = mid + 1

            if answer is None:
                return 366
            return answer

        

        for i in range(len(days) - 1, -1, -1):

            dp[days[i]] = min(costs[0]+ dp[next_greater(days[i]+1)], costs[1]+dp[next_greater(days[i]+7)], costs[2]+dp[next_greater(days[i]+30)])
            
        
        return dp[days[0]]