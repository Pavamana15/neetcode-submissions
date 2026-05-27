# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         common = list(strs[0])
#         first_char = strs[0][0]

#         for s in strs[1:]:
#             print("The current string is:", s)

#             if s[0] == first_char:
                
#                 common = [ch for ch in common if ch in s]
#             else:
#                 common = []
#                 break

#             print("The common set is:", common)

#         return "".join(common)



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]






        