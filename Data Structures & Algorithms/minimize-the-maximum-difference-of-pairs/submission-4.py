class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return p
        nums.sort()

        def pairs(val):
            count = 0
            i, j = 0, 1
            while i < len(nums) and j < len(nums):
                if nums[j] - nums[i] <= val:
                    count += 1
                    j += 2
                    i += 2
                else:
                    i += 1
                    j += 1
               
                
  
            print(f" The mid val : {val} | The count : {count}")
            return count >= p
        left,right = 0, nums[-1] - nums[0]

        print(f"The left : {left} |  The right : {right}")
        print("Binary Search is starting !!!!!!!!")
        
        while left < right:
            
            mid = left + (right - left) // 2
            print(f"The left : {left} |  The right : {right} | The mid : {mid}")
            if pairs(mid):
                right = mid 
            else:
                left = mid +1

        return left