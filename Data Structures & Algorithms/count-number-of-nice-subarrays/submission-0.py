class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(x):
            if x < 0:
                return 0
            res = l = cur = 0
            for r in range(len(nums)):
                if nums[r] % 2 == 1:
                    cur += 1
                while cur > x:
                    if nums[l] % 2 == 1:
                        cur -= 1
                    l += 1
                res += (r - l + 1)
            return res

        return helper(k) - helper(k-1)
