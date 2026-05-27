# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:

#         DP = [0]*(len(cost)+1)

#         DP[0 ] = 0
#         DP[1] = cost[0]
#         DP[2] = min(cost[0],cost[1])

#         for i in range(3,len(cost)+1):
#             DP[i] = min( DP[i-2] + cost[i-2], DP[i-3]+ cost[i-3])
        
#         return DP[len(cost)]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
