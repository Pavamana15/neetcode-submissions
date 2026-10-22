
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        left = answer = 0
        for right,x in enumerate(nums):
            while x-nums[left] > 2*k: left += 1
            answer = max(answer,right-left+1)
        return answer

