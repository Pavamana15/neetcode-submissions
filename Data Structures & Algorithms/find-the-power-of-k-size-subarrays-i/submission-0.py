class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        output = [-1] * (len(nums) - k + 1)
        left = 0

        for right in range(len(nums)):
            if right > 0 and nums[right] != nums[right - 1] + 1:
                left = right

            if right - left + 1 >= k:
                output[right - k + 1] = nums[right]

        return output
