class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left, output,max_count  = 0,0,0
        count = defaultdict(int)

        for right in range(len(nums)):
            # print(f"The current left : {left} | The current right : {right}")
            count[nums[right]] += 1
            max_count = max(max_count, count[nums[right]])
            # print(f"The current maximum count : {max_count}")

            while count[nums[right]] > k:
                count[nums[left]] -= 1
                
                left += 1
            
            
            output = max(output, right - left + 1)

        return output

