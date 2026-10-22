class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left, output,count = 0,0,0
        max_value = max(nums)


        for right in range(len(nums)):
            if nums[right] == max_value:
                count += 1

            
                
            while count >= k:
                output += len(nums) - right
                if nums[left] == max_value:
                    count -= 1
                left += 1

            
        

        return output
