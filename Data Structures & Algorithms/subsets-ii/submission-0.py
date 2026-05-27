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

        unique_res = []

        for subset in res:
            if sorted(subset) not in unique_res:
                unique_res.append(sorted(subset))

        print("The unique subsets are:", unique_res)

        return unique_res