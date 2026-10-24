class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        max_val = nums[0]
        min_val = nums[0]
        output = 0

        for right in range(len(nums)):
            max_val = max(max_val, nums[right])
            min_val = min(min_val, nums[right])
            print(f"The current position is :{ right}")
            print(f"The current maximum value : {max_val} | The minimum value : {min_val}")
            print(f"The current value : {nums[right]}")

            

            
            while left <= right  and max_val - min_val > limit:

                if nums[left] == max_val:
                    max_val = nums[left+1]
                if nums[left] == min_val:
                    min_val = nums[left+1]
                
                left += 1

            if abs(max_val - nums[right]) <= limit and abs(nums[right] - min_val)<= limit:
                output = max(output, right - left +1)
                
                print(f"!!!***!!!*****!!******!!!!!!!****")
                print(f"The subarray found at from left : {left} to right : {right}")
                print(f"The current output : {output}")
                    

                    


        return output