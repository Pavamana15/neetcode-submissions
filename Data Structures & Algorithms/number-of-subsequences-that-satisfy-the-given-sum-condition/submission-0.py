class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        output = 0
        nums.sort()

        for i in range(len(nums)):
            cur_min = nums[i]

            if cur_min > target or cur_min + cur_min > target:
                return output % (10**9 + 7)

            
            for j in range(i, len(nums)):
                
                if cur_min + nums[j] <= target:
                    if j == i:
                        output += 1
                    else:
                        output += 2**(j-i-1)
                

        return output % (10**9 + 7)