class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        left , output = 0,0

        for right in range(len(nums)):
            product = product * nums[right]

            while left < right and product >= k:
                product = product / nums[left]
                left += 1

            if product < k:
                output += right - left + 1 
                

        return output