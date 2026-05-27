# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         left = right = 0
#         s1_sublist = []
#         s2_sublist = []

#         def is_ordered_subsequences(subs, s):
#             pos = 0
#             for sub in subs:
#                 for ch in sub:
#                     pos = s.find(ch, pos)
#                     if pos == -1:
#                         return False
#                     pos += 1
#             return True

#         if not s1 and not s2 and not s3:
#             return True

        
#         while left != len(s3) or right != len(s3):
#             print("The left value is:", left)
#             print("The right value is:", right)
#             while s3[right] in s1 and right != len(s3):
#                 print("We are in s1")
#                 print("The left value is:", left)
#                 print("The right value is:", right)
#                 right += 1
#                 if right == len(s3):
#                     break

#             s1_sublist.append(s3[left:right])
#             left = right

#             print("We are out of S1")
#             print("The right value is:", right)

#             if right == len(s3):
#                 break

#             while s3[right] in s2 and right != len(s3):
#                 print("We are in s2")
#                 print("The left value is:", left)
#                 print("The right value is:", right)
#                 right += 1
#                 if right == len(s3):
#                     break

            
#             s2_sublist.append(s3[left:right])
#             left = right

#         print("The S1 sub list is:",s1_sublist)
#         print("The S2 sub list is:",s2_sublist)

#         if abs(len(s1_sublist) - len(s2_sublist)) <= 1 and is_ordered_subsequences(s1_sublist, s1) and is_ordered_subsequences(s2_sublist, s2):
#             return True
#         else:
#             return False
            
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]
