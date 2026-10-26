class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0

        output = float('inf')

        for right in range(len(nums)):
            if right - left + 1 == k:
                output = min(output, nums[right] - nums[left])

                left += 1
        return output