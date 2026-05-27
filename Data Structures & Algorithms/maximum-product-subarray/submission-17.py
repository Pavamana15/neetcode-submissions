# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         dp = nums
#         maxProduct = math.prod(dp)

#         # if len([num for num in nums if num < 0]) % 2 == 0:
#         #     dp = [abs(num) for num in nums]
#         # else:
#         #     dp = nums
    
#         #dp[0] = nums[0]
#         # for i in range(1, len(dp)):  
#         #     dp[i] = dp[i] * dp[i-1]  
#         for i in range(1, len(nums)):
#             # current_Product = nums[i]*dp[i-1]
#             # if current_Product < dp[i-1] :
#             #     dp[i] = 1
#             # else:
#             dp[i] =  max(nums[i]*dp[i-1], dp[i])

            

#         return max(max(dp), maxProduct)
#         # left , right = 0,0
#         # maxProduct = [-5]
#         # Product = 1

#         # while right != len(nums):
#         #     Product = Product * nums[right]

#         #     if Product < maxProduct[-1] :
#         #         right += 1
#         #         left = right
#         #         Product = 1

#         #     else:
#         #         maxProduct.append(Product)
#         #         right += 1

#         # return maxProduct[-1]

            
            
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res
