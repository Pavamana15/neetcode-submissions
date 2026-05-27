class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        original = matrix
        
        def Binary_Search(nums):
            if len(nums) == 1:
                return True if nums[0] == target else False
            else:
                leftMid = int(len(nums) / 2) - 1
                rightMid = int(len(nums) / 2)
                
                if target <= nums[leftMid]:
                    return Binary_Search(nums[:leftMid+1])
                else:
                    return Binary_Search(nums[rightMid:])

        return Binary_Search([item for row in matrix for item in row]
)