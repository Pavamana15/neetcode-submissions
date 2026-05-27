import numpy as np
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if np.size(np.unique(nums)) == np.size(nums):
            return False
        else:
            return True
         