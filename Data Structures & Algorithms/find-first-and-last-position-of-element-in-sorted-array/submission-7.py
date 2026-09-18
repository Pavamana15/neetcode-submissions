class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0 , len(nums)-1
        output  = [-1,-1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                l1 = left
                r1 = mid

                while l1 <= r1:
                    m1 = l1 + (r1-l1)//2

                    if nums[m1] < target:
                        l1 = m1 +1
                    else:
                        r1 = m1 -1

                output[0] = l1

                l1 = mid
                r1 = right

                while l1 <= r1:
                    m1 = l1 + (r1-l1)//2

                    if nums[m1] > target:
                        r1 = m1 -1
                    else:
                        l1 = m1 + 1 



                output[1] = l1-1

                return output



                
                


        return output