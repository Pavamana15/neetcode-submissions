class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        output , total ,left  = 0,0,0
        count = defaultdict(int)

        for right in range(len(nums)):
            
            
            if right == 0:
                total += nums[0]
                count[nums[right]] += 1
            
            if right > 0 and nums[right] != nums[right-1]:
                count[nums[right]] += 1
                total += nums[right]
            
            

            if right - left + 1 > k:
                if nums[left] != nums[left +1]:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    total -= nums[left]
                left += 1


            if right - left + 1 == k and len(count) == k:
                output = max(output, total)

        return output
