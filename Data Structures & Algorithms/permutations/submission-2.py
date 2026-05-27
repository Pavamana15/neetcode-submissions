class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if len(subset)== len(nums):
                res.append(subset.copy())
                return
            

            for j in range(len(nums)):

                
                
                if nums[j] not in subset :
                    subset.append(nums[j])
                    dfs(j+1)
                    subset.pop()

        dfs(0)
        return res