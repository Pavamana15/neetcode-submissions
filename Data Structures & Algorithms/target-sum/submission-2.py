class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0

        def dfs(i, a):
            if i == len(nums):
                return 1 if a == target else 0
            return dfs(i + 1, a + nums[i]) + dfs(i + 1, a - nums[i])

                

        return dfs(0,0)