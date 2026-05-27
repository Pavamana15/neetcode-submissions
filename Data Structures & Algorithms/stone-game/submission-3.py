class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        stoneSum = sum(piles)
        target = (stoneSum + 1) // 2
        dp = {}

       
        



        def dfs(i,j, total):
            if total >= target or i > j:
                return total - (stoneSum - total)
            if (i,j, total) in dp:
                return dp[(i,j, total)]

            # if piles[i] > piles[j]:
            #     dp[(i, j,total)] = dfs(i+2,j,total + piles[i])
            # elif piles[i] < piles[j]:
            #     dp[(i, j,total)] = dfs(i,j-2,total + piles[j])
            # else:
            dp[(i,j, total)] = max(dfs(i + 2, j,total+piles[i]), dfs(i ,j-2, total + piles[j]))


            
            return dp[(i, j,total)]

        return dfs(0,len(piles) - 1, 0) > 0