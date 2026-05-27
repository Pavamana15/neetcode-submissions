class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = float('inf')

        if min(nums)> 1 or max(nums) <= -1:
            return 1

        if min(nums) < 0 and max(nums) > 1 and 1 not in nums:
            return 1
        

        for num in nums:
            if num + 1 not in nums  and num+1 > 0:
                print("The number not found:", num+1)
                
                res = min(res,num+1)

        return res