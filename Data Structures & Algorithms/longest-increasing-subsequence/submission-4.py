# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         start_number = min(nums)
#         start_index = nums.index(start_number)
        
#         res = [ start_number]
#         # for i in range(start_index, len(nums)):
        
#         # 
#         for i in range(start_index+1, len(nums)):
#             print("The current result is:",res)
#             if nums[i] > res[-1]:
#                 res.append(nums[i])
#             elif nums[i] < res[-1] and nums[i] > res[0]:
#                 res.remove(res[-1])
#                 res.append(nums[i])
#                 print("The last element is removed")
#                 #continue
        


#         print("The final result is:",res)
#         return len(res)

 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
