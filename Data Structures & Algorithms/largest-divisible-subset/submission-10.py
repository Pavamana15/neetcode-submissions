class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        LIS = [1] * len(nums)
        subset = []
       

        for i in range(len(nums) - 1, -1, -1):
            
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
                   
        print("LIS is :", LIS)
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res = [nums[i]]
            cur = 0
            for j in range(i + 1, len(nums)):
                if nums[j] % res[-1] == 0 and LIS[j] +1 == LIS[i]- cur:
                    res.append(nums[j])
                    cur += 1
                

            subset.append(res)

        print("The subset is :", subset)
        subset.sort(key=len, reverse=True)
        return subset[0]




        

        
            
            



