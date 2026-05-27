# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
        
#         temp = coins.copy()
#         def maxsum(money, target,res):
#             if len(money) == 1 and money[0] <= target:
#                 if target % money[0] == 0:
#                     res += target // money[0]
#                     # for _ in range(target // money[0]):
#                     #     res.append(money[0])

#                     return res

#                 else:
#                     return -1
            

#             if len(money) == 1 and money[0] > target and target == 0:

#                 return res

#             if len(money) == 1 and money[0] > target and target > 0:
#                 return -1

#             # if money and target != 0 :
#             #     return -5

#             if not money or target == 0:
#                 print("Money list is empty and returning the result")
#                 print("The target is :", target)
#                 return res

            

#             print("The current maximum value is :", max(money))
#             print("THe current money list is:", money)
#             print("The current target is :", target)
            
#             if max(money) > target :
#                 while max(money)  > target:
#                     max_value = max(money)  
#                     money.remove(max_value)
#                     if not money:
#                         break

#                 print("The money list after reomving maximum values:",money)

#                 if (not money and target != 0) or (money and min(money) > target):
#                     print("Target is not zero,but money list is empty")
#                     return -5

#             if money:
#                 print("The current maximum value is :", max(money))
#                 print("THe current money list is:", money)
            
#                 res += target // max(money)
#                 max_value = max(money)  
#                 money.remove(max_value)
#                 target -= (target // max_value)*max_value

#             if money:
#                 print("The next maximum value is :", max(money))
#                 print("THe next money list is:", money)
#                 print("The next target is :", target)
#             else:
#                 print("The current money list is empty")

#             print("The present output is:", res)

            
            
            
            



           

            
#             return maxsum(money, target - (target // max_value)*max_value,res)

         
#         output = maxsum(coins,amount,0)

#         if output == -5:
#            print("We have to restart")
#            print("The coins list is:", temp)
#            max_value = max(temp)  
#            temp.remove(max_value)
#            output = maxsum(temp,amount, 0)
#         print("The final output is :", output)
        
        
#         return output


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
