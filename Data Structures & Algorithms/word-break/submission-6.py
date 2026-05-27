# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         left, right = 0,len(s)

#         # while right != len(s):
#         #     # while s[left:right+1] not in wordDict and right != len(s):
#         #     #     right += 1
#         #     print("The present string is:", s)
#         #     if s[left:right+1]  in wordDict:
#         #         s = s[:left] + s[right+1:]
#         #         right = 0
#         #         left = 0

#         #         # if s in wordDict:
#         #         #     s = " "
#         #         #     break

#         #     else:
#         #         right += 1

#         while right != 0:
#             print("The present string is:", s)
#             print("The left is:",left)
#             print("The right is :",right)
#             if s[left:right] in wordDict:
#                 s = s[right:]
#                 right = len(s)

#             else:
#                 right -= 1



#         print("The remaining string is :", s)
#         return True if not s else False

        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
