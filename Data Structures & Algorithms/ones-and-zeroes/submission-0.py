class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        cache = {}
        def dfs(i,x,y):
            if (i,x,y) in cache:
                return cache[(i,x,y)]
            if i == length :
                return 0

            

            

            cnt = Counter(strs[i])

            count = dfs(i+1,x,y)

            if x+cnt["0"] <= m and y+cnt["1"] <= n:
                count = max(1 + dfs(i+1,x+cnt["0"],y+cnt["1"]), count )

            
            cache[(i,x,y)] = count

            return cache[(i,x,y)]

        return dfs(0,0,0)