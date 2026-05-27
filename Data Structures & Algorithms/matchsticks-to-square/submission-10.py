class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # total_length = sum(matchsticks)
        # if total_length % 4 != 0:
        #     return False

        # length = total_length // 4
        # sides = [0] * 4
        # matchsticks.sort(reverse=True)

        # def dfs(i):
        #     if i == len(matchsticks):
        #         return True

        #     for side in range(4):
        #         if sides[side] + matchsticks[i] <= length:
        #             sides[side] += matchsticks[i]
        #             if dfs(i + 1):
        #                 return True
        #             sides[side] -= matchsticks[i]

        #         if sides[side] == 0:
        #             break

        #     return False

        # return dfs(0)

        k = 4
        if sum(matchsticks) % k != 0:
            return False

        matchsticks.sort(reverse=True)
        target = sum(matchsticks) // k
        used = [False] * len(matchsticks)

        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0, k - 1, 0)
            for j in range(i, len(matchsticks)):
                if used[j] or subsetSum + matchsticks[j] > target:
                    continue
                used[j] = True
                if backtrack(j + 1, k, subsetSum + matchsticks[j]):
                    return True
                used[j] = False
            return False

        return backtrack(0, k, 0)