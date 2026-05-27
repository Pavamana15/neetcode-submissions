class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        min_steps = [0]* (len(nums) + max(nums))

        
        min_steps[len(nums)-2] = 1

        for i in range(len(nums)-3,-1,-1):
            min_steps_val = 1 + min_steps[i+1]
            for step in range(1,nums[i]+1):
                min_steps_val = min(min_steps_val, 1 + min_steps[step+i] )
                

            min_steps[i] = min_steps_val

        return min_steps[0]
       
