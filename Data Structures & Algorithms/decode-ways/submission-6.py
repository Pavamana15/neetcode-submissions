# class Solution:
#     def numDecodings(self, s: str) -> int:

#         def find_combinations(arr, target):
#                 memo = {}  # To store solutions for subproblems (dynamic programming)
                
#                 def helper(target):
#                     # If the target is already in the memo, return the cached result
#                     if target in memo:
#                         return memo[target]
                    
#                     # If the target is an empty string, there's one way to make it (no elements needed)
#                     if target == "":
#                         return 1
                    
#                     # Initialize the number of ways to make the target
#                     ways = 0
                    
#                     # Try every element in arr as a potential prefix of the target
#                     for elem in arr:
#                         # If the target starts with the current element, recursively check the rest of the target
#                         if target.startswith(elem):
#                             remaining_target = target[len(elem):]  # Substring after the prefix
#                             ways += helper(remaining_target)  # Recursively calculate the ways for the rest
                    
#                     # Store the result in memo for this target
#                     memo[target] = ways
#                     return ways
                
#                 # Call the helper function with the full target string
#                 return helper(target)
#         res = []
#         left ,right = 0,0
#         i = 0

#         while left != len(s) :
#             print("The left is:",left)
            
            
#             if 1 <= int(s[left]) <= 26 :
#                 res.append(s[left])

#             left = left +1
        
#         print("The valid numbers are:", res)
#         left,right = 0,1
#         while right != len(s):
#             print("The left is:",left)
#             print("The right is :", right)
#             print("The first digit is:", s[left])

#             if 1 <= int(s[left:right+1]) <= 26 and int(s[left]) != 0 :
#                 res.append(s[left:right+1])

#             left += 1
#             right +=1 
        
#         print("The valid numbers are:", res)

#         valid_combinations = find_combinations(res, s)
#         # return len(res) - len(s) +1 if res else 0

#         return valid_combinations

        
# Memoization solution 
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)

# Dynamic Programming solution
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         dp = {len(s): 1}
#         for i in range(len(s) - 1, -1, -1):
#             if s[i] == "0":
#                 dp[i] = 0
#             else:
#                 dp[i] = dp[i + 1]

#             if i + 1 < len(s) and (
#                 s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
#             ):
#                 dp[i] += dp[i + 2]
#         return dp[0]
