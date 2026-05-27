class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # original = nums

        # def Binary_Search(nums):

        #     L = 0
        #     R = len(nums)-1
        #     M = L + (R - L)//2

        #     if len(nums) == 1:
        #         if target == nums[0]:
        #             return original.index(nums[0])
        #         else:
        #             return original.index(nums[0]) + 1
            

        #     if target > nums[M]:
        #          return Binary_Search(nums[M:])
        #     else:
        #         return Binary_Search(nums[:M])



        l, r = 0, len(nums) - 1

        while l <= r:
            print("The present left is : ",l)
            print("The present right is : ",r)
            
            if r == l:
                print("THe left and right are equal: ",l)
                if nums[l] == target:
                    return l
                elif nums[l] > target:
                    return l
                else:
                    return l+1
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m -1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        if r < l:
            if nums[r] == target:
                    return r
            elif nums[r] > target:
                    return max(r-1,0)
            else:
                    return r+1

        

        
        

             
