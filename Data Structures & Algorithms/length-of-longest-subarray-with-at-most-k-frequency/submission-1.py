class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left, output,max_count  = 0,0,0
        count = defaultdict(int)

        for right in range(len(nums)):
            
            count[nums[right]] += 1
        
            
            while count[nums[right]] > k:
                output = max(output, right - left)
                count[nums[left]] -= 1
                left += 1


            
            
            

        return max(output,right - left + 1)

