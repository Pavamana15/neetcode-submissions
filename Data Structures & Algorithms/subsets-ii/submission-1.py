class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)

        # unique_res = []

        
        res = [sorted(subset) for subset in res]

        unique_res = set(tuple(subset) for subset in res)

        unique_res = [list(subset) for subset in unique_res]
        
        print("The unique subsets are:", unique_res)

        return unique_res