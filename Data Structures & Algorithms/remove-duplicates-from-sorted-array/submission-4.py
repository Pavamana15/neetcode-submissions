class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1

        k = 1

        while i < len(nums) and j < len(nums):
            if nums[i] < nums[j]:
                i += 1
                j += 1
                k += 1
                continue
            else:
                while j < len(nums) and nums[i] == nums[j]:
                    del nums[j]
                    # j += 1
                    
                k += 1

        return k

        