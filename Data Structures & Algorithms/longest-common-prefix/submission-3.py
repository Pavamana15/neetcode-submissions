class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]  # full string

        for s in strs[1:]:
            print("The current string is:", s)

            # prefix-style shrinking
            i = 0
            while i < len(common) and i < len(s) and common[i] == s[i]:
                i += 1

            common = common[:i]

            print("The common set is:", list(common))


        return "".join(common)



# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         for i in range(len(strs[0])):
#             for s in strs:
#                 if i == len(s) or s[i] != strs[0][i]:
#                     return s[:i]
#         return strs[0]






        