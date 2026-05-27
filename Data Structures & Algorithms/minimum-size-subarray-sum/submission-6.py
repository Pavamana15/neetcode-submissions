class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums)+1

        

        

            




        for i in range(len(nums)):
            total = nums[i]

            if total >= target:
                res = min(res,1)
                return res

            for j in range(i+1, len(nums)):
                total += nums[j]
                if total >= target:
                    res = min (res,j-i+1)
                    break


        return res if res != len(nums)+1 else 0

