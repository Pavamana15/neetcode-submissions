class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []

        def backtrack(i,cur):
            if i == len(s):
                res.append(cur.copy())
                return
            
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    cur.append(s[i : i + len(w)])
                    backtrack(i+len(w),cur)
                    cur.pop()

                

        
        backtrack(0,[])
        print("The final result is :", res)
        final_res = []
        for sen in res:
            final_res.append(" ".join(sen))

        print("The final result after spacing is :", final_res)
        return final_res