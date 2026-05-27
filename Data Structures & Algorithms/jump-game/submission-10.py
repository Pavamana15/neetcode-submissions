# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         target = 0
#         num = 0
        
#         for i in range(len(nums)):
#             if i >= len(nums)-1:
#                 break
#             target += nums[i]
            
#             num += 1
        
#         return True if target >= len(nums)-1 else False
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
