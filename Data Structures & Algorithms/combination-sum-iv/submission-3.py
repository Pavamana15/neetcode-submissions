class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = []
        memo = {}

        def dfs(cur, total):
            if total == target:
                return 1

            if total > target:
                return 0

            if total in memo:
                return memo[total]

            ways = 0
            for num in nums:
                cur.append(num)
                ways += dfs(cur, total + num)
                cur.pop()

            memo[total] = ways
            return ways


        return dfs([], 0)
