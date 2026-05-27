# class Solution:
#     def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
#         # cur = []
#         # res = []
#         # i = 0
        
#         # # for i in range(len(s)):
#         # while i < len(s):
#         #     found = False

#         #     for w in dictionary:
#         #         if i + len(w) <= len(s) and s[i:i+len(w)] == w:
#         #             cur.append(w)
#         #             found = True
#         #             i += len(w)
#         #             break
                    

#         #     if not found:
#         #         res.append(i)
#         #         i += 1

#         # return len(res) 

#         res = []
#         output = []

#         def backtrack(i,cur):
#             if i == len(s) :
                
#                 return

#             if i < len(s) and cur :
#                 output.append(cur.copy())
#                 backtrack(i+1,[])
                


#             found = False
#             for w in dictionary:
                
#                 if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
#                     found = True
#                     for j in range(i, i+len(w)):
#                         if j not in res:
#                             res.append(j)
#                     cur.append(s[i : i + len(w)])
#                     backtrack(i+len(w),cur)
#                     cur.pop()

#             if not found:
#                 backtrack(i+1,[])
                    

            

            
       

                

        
#         backtrack(0,[])
#         print("The final result is :", res)
#         # final_res = []
#         # for sen in res:
#         #     final_res.append(" ".join(sen))

       
        


      
#         #print("The final words found are :", output)

#         return len(s) - len(res) 
                    
            

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        n = len(s)
        memo = {}                     # 🔹 ADDED: memoization

        def backtrack(i):
            if i == n:
                return 0              # 🔹 CHANGED: return count, not modify global list

            if i in memo:             # 🔹 ADDED
                return memo[i]

            # 🔹 OPTION 1: skip this character (counts as 1 extra)
            ans = 1 + backtrack(i + 1)

            # 🔹 OPTION 2: try matching dictionary words
            for w in dictionary:
                if i + len(w) <= n and s[i:i+len(w)] == w:
                    ans = min(ans, backtrack(i + len(w)))

            memo[i] = ans             # 🔹 ADDED
            return ans

        return backtrack(0)


                

                    
                    
        
                

        
        
        


        
       