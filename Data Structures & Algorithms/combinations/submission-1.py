class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        res = []
        subset = []

        def dfs(i):
            if len(subset)== k:
                res.append(subset.copy())
                return
            

            for j in range(i,n):
                
                if nums[j] not in subset:
                    subset.append(nums[j])
                    dfs(j)
                    subset.pop()

        dfs(0)
        return res