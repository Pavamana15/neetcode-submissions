class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = []
        res = 0
        if len(nums) == 1:
            return nums[0]

        if all(x < 0 for x in nums):
            return max(nums)
        for n in nums:
            res = max(n+res,n,0)
            output.append(res)

        print("The maximum sum is :", output) 
        return max(output)