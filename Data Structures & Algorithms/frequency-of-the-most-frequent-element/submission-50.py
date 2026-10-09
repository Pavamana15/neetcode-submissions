class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        left,right = 0,1

        cum_sum = [0]

        for num in nums:
            cum_sum.append(cum_sum[-1] + num)

        while right < len(nums) and k:

            
            
            if nums[right] == nums[left]:
                res = max(res, right - left + 1)
                right += 1
                
                
            else:
                if k - ((nums[right])*(right - left+1) - (cum_sum[right+1] - cum_sum[left]) ) >= 0:
                    
                    
                    
                    res = max(res, right - left+1)
                    right += 1
                
                else:
                    left +=1
                    
                    
        

       
        return res





        