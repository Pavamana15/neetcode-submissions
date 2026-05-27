# class Solution:
#     def stoneGame(self, piles: List[int]) -> bool:
        
#         stoneSum = sum(piles)
#         target = (stoneSum + 1) // 2
#         dp = {}

       
        



#         def dfs(i,j, total):
#             if total >= target or i > j:
#                 print("Alice total is :", total)
#                 return total - (stoneSum - total)
#             if (i,j, total) in dp:
#                 return dp[(i,j, total)]

            
#             dp[(i,j, total)] = max(dfs(i + 2, j,total+piles[i]), dfs(i ,j-2, total + piles[j]))


            
#             return dp[(i, j,total)]

#         return dfs(0,len(piles) - 1, 0) > 0

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def dfs(i, j):
            if i > j:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = max(
                piles[i] - dfs(i + 1, j),
                piles[j] - dfs(i, j - 1)
            )
            return dp[(i, j)]

        return dfs(0, len(piles) - 1) > 0










