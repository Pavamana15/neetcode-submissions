class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right, output,zero = 0,0,0,0

        while right < len(nums):
            # print(f"The current left : {left} | The current right : {right}")
            if nums[right] == 1:
                right += 1
                
            else:
                if zero == k:
                    output = max(output, right-left)
                    
                    if nums[left] == 0:
                        zero -= 1
                    left += 1
                else:
                    zero += 1
                    right += 1
            # print(f"The output is : {output}")
        return max(output, right - left)