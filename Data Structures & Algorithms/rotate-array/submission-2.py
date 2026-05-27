class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = 'a'
        k = k % len(nums)
        while k > 0:
            for i in range(len(nums)-2,-1,-1):
                temp = nums[i+1]
                nums[i+1] = nums[i]
                nums[i] = temp
            # print("The current number list is:", nums)
            k -= 1
                