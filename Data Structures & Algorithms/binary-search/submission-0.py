

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        original = nums
        
        def Binary_Search(nums):
            if len(nums) == 1:
                return original.index(nums[0]) if nums[0] == target else -1
            else:
                leftMid = int(len(nums) / 2) - 1
                rightMid = int(len(nums) / 2)
                
                if target <= nums[leftMid]:
                    return Binary_Search(nums[:leftMid+1])
                else:
                    return Binary_Search(nums[rightMid:])

        return Binary_Search(nums)
