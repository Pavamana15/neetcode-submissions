# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         if len(text1)==0 or len(text2)==0 or (len(text1)==0 and len(text2)==0) :
#             return 0

#         if text1 == text2:
#             return len(text1)

#         ASCII_text1 = [ord(char) for char in text1]
#         ASCII_text2 = [ord(char) for char in text2]
#         longer_list = ASCII_text1 if len(ASCII_text1) > len(ASCII_text2) else ASCII_text2
#         print("The text 1 is :", ASCII_text1)
#         print("The text 2 is :", ASCII_text2)
#         print("Longer list is :", longer_list)
        
#         if len(ASCII_text1) > len(ASCII_text2):
#             intersection = [item for item in ASCII_text2 if item in set(ASCII_text1)]
#         else:
#             intersection = [item for item in ASCII_text1 if item in set(ASCII_text2)]
#         print("The final intersection is :", intersection)
#         indices_in_longer_list = []
#         for item in intersection:
#             print("The item is :", item)
#             if item in longer_list:
#                 index = longer_list.index(item)
#                 print("The index is :", index)
#                 indices_in_longer_list.append(longer_list.index(item))
#                 longer_list[longer_list.index(item)] = 0
#                 print("Longer list after finding the index is :", longer_list)
#             else:
#                 print("Item not found:", item)

#         #indices_in_longer_list = [longer_list.index(item) for item in intersection]
        
#         print(" Indices of intersection is :", indices_in_longer_list)
#         if not intersection :
#             return 0
#         else:
#             LIS = [1] * len(indices_in_longer_list)
            
#             for i in range(len(indices_in_longer_list) - 1, -1, -1):
#                 for j in range(i + 1, len(indices_in_longer_list)):
#                     if indices_in_longer_list[i] < indices_in_longer_list[j]:
#                         LIS[i] = max(LIS[i], 1 + LIS[j])

#             print("Output is :",max(LIS))
#             return max(LIS)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] 
                 for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]