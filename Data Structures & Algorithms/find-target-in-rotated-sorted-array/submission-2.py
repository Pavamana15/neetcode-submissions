class Solution:
    def search(self, nums: List[int], target: int) -> int:
        original = nums
        left , right = 0 , len(nums)-1

        
        def Binary_Search(nums):
            print("The present nums list is :", nums)
            if len(nums) == 1:
                return original.index(nums[0]) if nums[0] == target else -1
            else:
                leftMid = 0
                rightMid = len(nums)-1

                mid = (leftMid + rightMid) // 2

                if nums[mid] == target:
                   print("Search is successful and found",nums[mid])
                   return original.index(nums[mid])
                else:
                    if nums[mid] >= nums[leftMid]:
                        if target > nums[mid] or target < nums[leftMid]:
                            return Binary_Search(nums[mid+1:])
                        else:
                            return Binary_Search(nums[:mid])
                    else:
                        if target < nums[mid] or target > nums[rightMid]:
                            return  Binary_Search(nums[:mid])
                        else:
                            return Binary_Search(nums[mid+1:])


                
                    # if (nums[mid] >= nums[leftMid] and nums[leftMid] > target) or ( nums[mid] >= nums[leftMid] and nums[leftMid] < target):
                    #     return Binary_Search(nums[mid+1:])
                    # elif nums[leftMid] < target < nums[mid] or (nums[mid] < nums[leftMid] and target > nums[leftMid]) :
                    #     return Binary_Search(nums[:mid])
                     

        return Binary_Search(nums)