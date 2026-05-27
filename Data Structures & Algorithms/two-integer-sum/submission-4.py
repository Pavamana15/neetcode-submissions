import numpy as np
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = []
        nums = np.array(nums)
        for i in range(nums.shape[0]):
            for j in range(i+1, nums.shape[0]):
                    if nums[i]+ nums[j] == target:
                        ind.append(i)
                        ind.append(j)
                        return ind

