class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if len(nums) == 1:
                break
            if num in nums[:i] + nums[i+1:]:
                nums = [x for x in nums if x != num]

            print("Remaining numbers are:", nums)
        
        print("Remaining numbers are:", nums)
        return nums[0]
