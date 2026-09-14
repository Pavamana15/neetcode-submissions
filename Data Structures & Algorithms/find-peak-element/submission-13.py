class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            
            m = l + ((r - l) // 2)
            print(f"The left : {l} | The right : {r} | The mid : {m}")
            if m - 1 < 0:
                left_peak = -float("inf")
            else:
                left_peak = nums[m-1]

            if m + 1 == len(nums):
                right_peak = -float("inf")
            else:
                right_peak = nums[m+1]
            
            if (( left_peak <= nums[m]) and
                ( nums[m] >= right_peak)  ):
                print("Returning !!!!!!")
                return m
            
            

            if left_peak < nums[m] < right_peak:
                l = m+1
                print(f" The left is incrementing")
            else:

                r = m - 1
                print(f" The right is decrementing")

        print(f"Printing outside while loop : {l}")
        return l  