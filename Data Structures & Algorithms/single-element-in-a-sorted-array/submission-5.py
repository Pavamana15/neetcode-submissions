class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
       

        if len(nums) == 1:
            return nums[0]

        
            


        def BS(left, right):
            print(f"The left : {left}  | right :  {right}")
            if left >= right and left != len(nums) -1 :
                return -1

            if left == right and left == len(nums) -1:
                return nums[left]
            
            if right - 1 == left and nums[left] < nums[right]:
                return nums[left]

            


            mid = left + (right - left) // 2

            print(f"The left : {left} | mid : {mid} | right :  {right}")

            # if right - 1 == mid and mid - 1 == left:
            #     if nums[left] < nums[mid] < nums[right]:
            #         return nums[mid]
                
           
            if nums[mid -1] == nums[mid]:
                mid = mid -1

            val1 = BS(left,mid)
            if nums[mid] == nums[mid+1]:
                mid = mid +1
            val2 = BS(mid+1,right)
            
            print(f"The value 1 : {val1} and value 2 : {val2}")
            if val1 >= 0:
                return val1
            elif val2 >= 0:
                return val2
            else:
                return -1


        return BS(0,len(nums)-1)

        